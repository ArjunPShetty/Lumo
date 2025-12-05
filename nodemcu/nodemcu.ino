/*
  lumo_esp8266.ino
  NodeMCU ESP8266 sketch (Arduino IDE)

  Function:
  - Connect to WiFi
  - On wake trigger (button) record a short audio snippet from A0 (analog mic)
  - POST the raw audio bytes to the Python server /api/upload_audio
  - Receive JSON response with speakText and audio_url
  - Download mp3 reply to SD card as /reply.mp3
  - Ask DFPlayer Mini to play reply.mp3

  Wiring notes (example):
  - A0 : analog microphone output (use amplifier module suited for ESP ADC)
  - SD Card: CS -> D8(GPIO15), MOSI->D7(GPIO13), MISO->D6(GPIO12), SCK->D5(GPIO14)
  - DFPlayer RX -> GPIO13 (D7) via voltage divider (DFPlayer RX is 5V tolerant? check module)
  - DFPlayer TX -> GPIO12 (D6) 
  - Button (wake) -> D3(GPIO0) with pullup to 3.3V (or use any digital pin)
  - Replace pins if your wiring differs.

  Libraries required:
    - ESP8266WiFi
    - SD (ESP8266 core)
    - SoftwareSerial

  IMPORTANT:
    - Sampling via analogRead on ESP8266 is low-quality (low rate). This sketch records a very low-fidelity clip
      sufficient for cloud recognition in many cases but not studio quality. For better audio use I2S mic + ESP32.
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <SD.h>
#include <SPI.h>
#include <SoftwareSerial.h>
#include <ArduinoJson.h>   // For parsing JSON (install via Library Manager)

// ---------- CONFIG ----------
const char* SSID = "YOUR_WIFI_SSID";
const char* PASSWORD = "YOUR_WIFI_PASSWORD";

const char* SERVER_IP = "192.168.1.100"; // change to your PC's IP
const uint16_t SERVER_PORT = 5000;

const int WAKE_BUTTON_PIN = D3;  // change to your wake button pin
const int LED_PIN = LED_BUILTIN; // status LED

// SD card pins (default for NodeMCU SPI)
const int SD_CS_PIN = D8; // D8 = GPIO15
// DFPlayer serial pins (to control module)
const int DFPLAYER_RX = D7; // connect to DFPlayer TX
const int DFPLAYER_TX = D6; // connect to DFPlayer RX (with level shifting if needed)

const char* REPLY_FILENAME = "/reply.mp3"; // saved on SD

// Recording parameters
const unsigned long SAMPLE_COUNT = 2000; // number of analog samples to send
const unsigned int SAMPLE_DELAY_US = 500; // approx sampling interval -> ~2000 Hz (adjust as needed)

// ---------- GLOBALS ----------
WiFiClient client;
SoftwareSerial dfSerial(DFPLAYER_RX, DFPLAYER_TX); // RX, TX to DFPlayer
bool sdInitialized = false;

// ---------- DFPlayer helper (minimal control) ----------
void dfplay_init() {
  dfSerial.begin(9600);
  delay(200);
}

void dfplayer_send_cmd(uint8_t *cmd) {
  // DFPlayer expects 10-byte packets; using simplified implementation
  for (int i = 0; i < 10; i++) dfSerial.write(cmd[i]);
}

// Play first file on SD named 0001.mp3; we will save reply as 0001.mp3 for DFPlayer's convenience
void dfplayer_play_file_index(uint16_t index) {
  // Build command (play track by index)
  uint8_t cmd[10] = {0x7E, 0xFF, 0x06, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0xEF};
  cmd[5] = (index >> 8) & 0xFF;
  cmd[6] = index & 0xFF;
  dfplayer_send_cmd(cmd);
}

void dfplayer_stop() {
  uint8_t cmd[10] = {0x7E,0xFF,0x06,0x16,0x00,0x00,0x00,0x00,0x00,0xEF};
  dfplayer_send_cmd(cmd);
}

// ---------- SD helper ----------
bool sd_setup() {
  if (!SD.begin(SD_CS_PIN)) {
    return false;
  }
  return true;
}

String httpPostAudioAndGetResponse(const uint8_t* data, size_t len) {
  HTTPClient http;
  String url = String("http://") + SERVER_IP + ":" + String(SERVER_PORT) + "/api/upload_audio";
  http.begin(client, url);
  http.addHeader("Content-Type", "application/octet-stream");
  int httpCode = http.POST((uint8_t*)data, len);
  String payload = "";
  if (httpCode > 0) {
    payload = http.getString();
  }
  http.end();
  return payload;
}

bool downloadFileToSD(const String &fileUrl, const char* sdPath) {
  // Simple HTTP GET
  HTTPClient http;
  http.begin(client, fileUrl); 
  int httpCode = http.GET();
  if (httpCode != HTTP_CODE_OK) {
    http.end();
    return false;
  }

  WiFiClient *stream = http.getStreamPtr();
  File f = SD.open(sdPath, FILE_WRITE);
  if (!f) {
    http.end();
    return false;
  }

  uint8_t buf[512];
  while (http.connected() && stream->available()) {
    size_t size = stream->available();
    if (size > sizeof(buf)) size = sizeof(buf);
    int c = stream->readBytes(buf, size);
    f.write(buf, c);
  }
  f.close();
  http.end();
  return true;
}

// ---------- Recording (very simple ADC sampling) ----------
void recordAndSend() {
  // allocate buffer
  uint8_t *buffer = (uint8_t*)malloc(SAMPLE_COUNT);
  if (!buffer) return;

  digitalWrite(LED_PIN, LOW); // turn on LED (active low on NodeMCU builtin LED)
  // sample A0
  for (unsigned long i = 0; i < SAMPLE_COUNT; i++) {
    int v = analogRead(A0); // 0..1023
    // map to 0..255
    uint8_t b = (uint8_t)((v >> 2) & 0xFF);
    buffer[i] = b;
    delayMicroseconds(SAMPLE_DELAY_US);
  }
  digitalWrite(LED_PIN, HIGH);

  // POST to server
  String resp = httpPostAudioAndGetResponse(buffer, SAMPLE_COUNT);
  free(buffer);

  if (resp.length() == 0) {
    Serial.println("No response from server.");
    return;
  }

  // Parse JSON (ArduinoJson recommended)
  StaticJsonDocument<1024> doc;
  DeserializationError err = deserializeJson(doc, resp);
  if (err) {
    Serial.print("JSON parse error: ");
    Serial.println(err.c_str());
    return;
  }

  const char* displayText = doc["displayText"] | "";
  const char* speakText = doc["speakText"] | "";
  const char* audio_url = doc["audio_url"] | "";

  Serial.println("Server displayText:");
  Serial.println(displayText);
  Serial.println("Server speakText:");
  Serial.println(speakText);
  Serial.println("audio_url:");
  Serial.println(audio_url);

  if (strlen(audio_url) > 0 && sdInitialized) {
    // Download audio to SD as 0001.mp3 (DFPlayer expects 0001.mp3 naming for index 1)
    String outUrl = String(audio_url);
    // Save temp as /0001.mp3
    const char* sdFilePath = "/0001.mp3";
    bool dl = downloadFileToSD(outUrl, sdFilePath);
    if (dl) {
      Serial.println("Downloaded reply to SD as 0001.mp3");
      // Ask DFPlayer to play index 1
      dfplayer_play_file_index(1);
    } else {
      Serial.println("Failed to download reply audio.");
    }
  } else {
    Serial.println("No audio_url or SD not initialized.");
  }
}

// ---------- Setup & Loop ----------
void setup() {
  Serial.begin(115200);
  pinMode(WAKE_BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH); // LED off (NodeMCU builtin LED is active low)

  // WiFi
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASSWORD);
  Serial.printf("Connecting to %s\n", SSID);
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 20000) {
    delay(500);
    Serial.print(".");
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println();
    Serial.print("Connected. IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println();
    Serial.println("WiFi connect failed.");
  }

  // DFPlayer
  dfplay_init();

  // SD
  sdInitialized = sd_setup();
  if (sdInitialized) {
    Serial.println("SD initialized.");
  } else {
    Serial.println("SD init failed. Ensure SD CS pin is correct.");
  }
}

void loop() {
  // Wait for wake button press (active LOW)
  if (digitalRead(WAKE_BUTTON_PIN) == LOW) {
    Serial.println("Wake button pressed. Recording audio...");
    // Debounce
    delay(50);
    while (digitalRead(WAKE_BUTTON_PIN) == LOW) delay(10);
    recordAndSend();
  }

  delay(50);
}
