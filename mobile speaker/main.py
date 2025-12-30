import os
import io
import uuid
import wave
import threading
import datetime
import speech_recognition as sr
import webbrowser
import sys
import pywhatkit
import pyttsx3
import psutil
import pyautogui
import wikipedia
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from conv_db import get_conversational_response

# ---------- CONFIG ----------
APP_NAME = "LUMO"
UPLOAD_DIR = "uploads"
AUDIO_DIR = os.path.join(UPLOAD_DIR, "audio")
REPLY_DIR = os.path.join(UPLOAD_DIR, "replies")
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(REPLY_DIR, exist_ok=True)

# Flask app
app = Flask(__name__)
CORS(app)

# TTS engine (shared for both modes)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)  # Female voice by default
engine.setProperty("rate", 170)
tts_lock = threading.Lock()

# Mode: will be set to 'cli' or 'api'
SERVER_MODE = None

def speak(audio):
    """Speak only in CLI mode."""
    if SERVER_MODE == "cli":
        engine.say(audio)
        engine.runAndWait()

def take_command():
    """Listen to user voice input or fallback to manual input (CLI only)."""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"[{APP_NAME}] Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language="en-in")
            print(f"[{APP_NAME}] You said: {query}")
            return query.lower()
    except Exception as e:
        print(f"[{APP_NAME}] Voice not working: {e}. Please type your command below:")
        return input(f"{APP_NAME} Command: ").lower()

def show_help():
    commands = f"""
=== {APP_NAME} - Available Commands ===

BASIC COMMANDS:
1. time                    - Get current time
2. open youtube/google     - Open websites
3. play <song>             - Play song on YouTube
4. search <query>          - Google search
5. open notepad/calculator/chrome - Open apps (Windows)

SYSTEM CONTROL:
6. shutdown / restart / logout    - System control (CLI only)
7. screenshot              - Take screenshot
8. mute                    - Mute system volume (Windows + nircmd)
9. battery                 - Show battery percentage

PRODUCTIVITY:
10. take a note            - Save a note
11. read notes             - Read saved notes

SETTINGS:
12. voice male/female      - Change assistant voice (CLI only)
13. help                   - Show this help menu
14. exit / quit            - Exit assistant (CLI only)
"""
    print(commands)
    speak("I have displayed the list of available commands on your screen.")
    return {"displayText": commands.strip(), "speakText": "I have displayed the list of available commands on your screen."}

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greet = "Good Morning!"
    elif 12 <= hour < 18:
        greet = "Good Afternoon!"
    else:
        greet = "Good Evening!"
    text = f"{greet} I am your AI Assistant {APP_NAME}. How can I help you?"
    speak(text)
    return {"displayText": text, "speakText": text}

def handle_query(query):
    """Main command processor. Returns dict {displayText, speakText}."""
    query = (query or "").lower().strip()
    if not query:
        text = "No command was detected. Please try again."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": "No command detected.", "speakText": text}

    # First, check for conversational responses
    chat_response = get_conversational_response(query)
    if chat_response:
        if SERVER_MODE == "cli":
            speak(chat_response)
        return {"displayText": chat_response, "speakText": chat_response}

    # Time
    if "time" in query and query.strip() == "time":
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"The time is {strTime}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Date
    if any(phrase in query for phrase in ["what day", "what date", "today's date"]):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        text = f"Today is {current_date}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Open websites
    if "open youtube" in query:
        webbrowser.open("https://youtube.com")
        text = "Opening YouTube..."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    if "open google" in query:
        webbrowser.open("https://google.com")
        text = "Opening Google..."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Play song on YouTube
    if query.startswith("play "):
        song = query.replace("play ", "", 1).strip()
        if not song:
            text = "Please specify a song to play."
            if SERVER_MODE == "cli":
                speak(text)
            return {"displayText": text, "speakText": text}
        pywhatkit.playonyt(song)
        text = f"Playing {song} on YouTube..."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Google search
    if query.startswith("search "):
        search_query = query.replace("search ", "", 1).strip()
        if not search_query:
            text = "Please specify what to search."
            if SERVER_MODE == "cli":
                speak(text)
            return {"displayText": text, "speakText": text}
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        text = f"Searching Google for '{search_query}'..."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Open apps (Windows)
    if query == "open notepad":
        try:
            os.startfile("notepad.exe")
            text = "Opening Notepad..."
        except Exception as e:
            text = f"Failed to open Notepad: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    if query == "open calculator":
        try:
            os.startfile("calc.exe")
            text = "Opening Calculator..."
        except Exception as e:
            text = f"Failed to open Calculator: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    if query == "open chrome":
        try:
            os.startfile("chrome.exe")
            text = "Opening Chrome..."
        except Exception as e:
            text = f"Failed to open Chrome: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # System controls (CLI only)
    if "shutdown" in query:
        if SERVER_MODE == "cli":
            text = "Shutting down your computer."
            speak(text)
            os.system("shutdown /s /t 1")
            return {"displayText": "System shutting down...", "speakText": text}
        else:
            text = "Shutdown is only allowed in CLI mode."
            return {"displayText": text, "speakText": text}

    if "restart" in query:
        if SERVER_MODE == "cli":
            text = "Restarting your computer."
            speak(text)
            os.system("shutdown /r /t 1")
            return {"displayText": "Restarting system...", "speakText": text}
        else:
            text = "Restart is only allowed in CLI mode."
            return {"displayText": text, "speakText": text}

    if "logout" in query:
        if SERVER_MODE == "cli":
            text = "Logging out now."
            speak(text)
            os.system("shutdown -l")
            return {"displayText": "Logging out...", "speakText": text}
        else:
            text = "Logout is only allowed in CLI mode."
            return {"displayText": text, "speakText": text}

    # Screenshot
    if "screenshot" in query:
        try:
            folder = "screenshots"
            os.makedirs(folder, exist_ok=True)
            i = 1
            while os.path.exists(os.path.join(folder, f"screenshot{i}.png")):
                i += 1
            filepath = os.path.join(folder, f"screenshot{i}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            text = f"Screenshot saved as {filepath}"
        except Exception as e:
            text = f"Could not take screenshot: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Mute system volume (Windows + nircmd)
    if query == "mute":
        try:
            os.system("nircmd.exe mutesysvolume 1")
            text = "System muted."
        except Exception as e:
            text = f"Could not mute system: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Battery status
    if query == "battery":
        battery = None
        try:
            battery = psutil.sensors_battery()
        except Exception:
            battery = None
        if battery:
            percent = battery.percent
            plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
            text = f"Battery is at {percent}% and it is {plugged}"
        else:
            text = "Battery information not available."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Notes
    if "take a note" in query:
        if SERVER_MODE == "cli":
            speak("What should I write in your note?")
            note = take_command()
            try:
                with open("notes.txt", "a", encoding="utf-8") as f:
                    f.write(note + "\n")
                text = "Note saved successfully."
            except Exception as e:
                text = f"Failed to save note: {e}"
            speak(text)
            return {"displayText": text, "speakText": text}
        else:
            text = "Taking notes via API is not supported. Use CLI mode to add notes."
            return {"displayText": text, "speakText": text}

    if "read notes" in query:
        try:
            if os.path.exists("notes.txt"):
                with open("notes.txt", "r", encoding="utf-8") as f:
                    notes = f.readlines()
                if notes:
                    text = "Your notes:\n" + "".join(f"- {n.strip()}\n" for n in notes)
                else:
                    text = "No notes found."
            else:
                text = "No notes found."
        except Exception as e:
            text = f"Could not read notes: {e}"
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Voice change
    if "voice" in query:
        if "male" in query:
            if len(voices) > 0:
                engine.setProperty("voice", voices[0].id)
            text = "Voice changed to male."
        elif "female" in query:
            if len(voices) > 1:
                engine.setProperty("voice", voices[1].id)
            text = "Voice changed to female."
        else:
            text = "Specify male or female voice."
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

    # Help
    if "help" in query:
        return show_help()

    # Exit (CLI only)
    if query in ("exit", "quit"):
        text = f"Goodbye! {APP_NAME} is shutting down. Have a nice day."
        if SERVER_MODE == "cli":
            speak(text)
            print(text)
            sys.exit(0)
        else:
            return {"displayText": "Exit command is only available in CLI mode.", "speakText": "Exit command is only available in CLI mode."}

    # Wikipedia / Info Fallback
    topic = query.replace("about ", "", 1).strip() if query.startswith("about ") else query.strip()
    try:
        if SERVER_MODE == "cli":
            speak(f"Searching Wikipedia for {topic}")
        summary = wikipedia.summary(topic, sentences=2, auto_suggest=False, redirect=False)
        if SERVER_MODE == "cli":
            speak(summary)
        return {"displayText": summary, "speakText": summary}
    except wikipedia.exceptions.PageError:
        text = f"Sorry, I couldn't find any page for {topic}. I will search for it on Google instead."
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}
    except wikipedia.exceptions.DisambiguationError as e:
        option = e.options[0]
        summary = wikipedia.summary(option, sentences=2, auto_suggest=False, redirect=False)
        if SERVER_MODE == "cli":
            speak(summary)
        return {"displayText": summary, "speakText": summary}
    except Exception:
        text = f"Couldn't find info for {topic}, searched online."
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        if SERVER_MODE == "cli":
            speak(text)
        return {"displayText": text, "speakText": text}

# ---------- Utility functions for audio processing ----------
def raw8_to_wav_bytes(raw_bytes, sample_rate=2000):
    """
    raw_bytes: bytes with values 0..255 (as sent from ESP)
    Convert to standard WAV (16-bit PCM, mono).
    """
    # Map 0..255 to -32768 .. 32767
    import array
    arr16 = array.array('h')  # 16-bit signed
    for b in raw_bytes:
        # convert unsigned to signed centered at 0
        centered = int(b) - 128
        val16 = int(centered * 256)  # scale to 16-bit range
        arr16.append(val16)
    # write wav to BytesIO
    bio = io.BytesIO()
    wf = wave.open(bio, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)  # 16-bit
    wf.setframerate(sample_rate)
    wf.writeframes(arr16.tobytes())
    wf.close()
    return bio.getvalue()

def save_tts_mp3(text, out_filename):
    """
    Save TTS output to mp3 using pyttsx3's save_to_file.
    Returns path to saved file.
    """
    # pyttsx3 can save to file in wav format
    wav_path = os.path.join(REPLY_DIR, out_filename + ".wav")
    mp3_path = os.path.join(REPLY_DIR, out_filename + ".mp3")
    
    with tts_lock:
        engine.save_to_file(text, wav_path)
        engine.runAndWait()
    
    # Try to convert wav -> mp3 using pydub if available
    try:
        from pydub import AudioSegment
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        os.remove(wav_path)
        return mp3_path
    except ImportError:
        print("Note: Install pydub for MP3 support. Using WAV format.")
        return wav_path
    except Exception:
        return wav_path

# ---------- Flask Routes ----------
@app.route("/")
def index():
    """Serve the main HTML page"""
    from flask import send_from_directory
    try:
        return send_from_directory(".", "index.html")
    except:
        return f"""
        <html>
        <head><title>{APP_NAME} Server</title></head>
        <body>
            <h1>{APP_NAME} Server is Running</h1>
            <p>Endpoints available:</p>
            <ul>
                <li>POST /api/command - Send text command</li>
                <li>POST /api/upload_audio - Upload audio from ESP8266</li>
                <li>POST /api/browser_voice - Upload audio from browser (mobile/laptop)</li>
                <li>GET /reply_audio/&lt;filename&gt; - Get TTS audio responses</li>
            </ul>
        </body>
        </html>
        """

@app.route("/api/command", methods=["POST"])
def api_command():
    """Handle text commands from web interface."""
    data = request.json or {}
    query = data.get("command", "")
    result = handle_query(query)
    return jsonify({
        "displayText": result.get("displayText", ""),
        "speakText": result.get("speakText", "")
    })

@app.route("/api/upload_audio", methods=["POST"])
def api_upload_audio():
    """
    Receive raw PCM audio from ESP8266, convert to text, process command,
    generate TTS response, and return audio URL.
    """
    try:
        raw = request.get_data()
        if not raw or len(raw) == 0:
            return jsonify({
                "displayText": "No audio received.",
                "speakText": "No audio received.",
                "audio_url": ""
            }), 400

        # Convert raw to wav bytes
        wav_bytes = raw8_to_wav_bytes(raw, sample_rate=2000)

        # Save incoming wav for debugging
        unique = str(uuid.uuid4())
        in_wav_path = os.path.join(AUDIO_DIR, f"{unique}.wav")
        with open(in_wav_path, "wb") as f:
            f.write(wav_bytes)

        # Recognize speech
        recognizer = sr.Recognizer()
        with sr.AudioFile(in_wav_path) as source:
            audio = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio, language="en-in")
            print(f"[{APP_NAME}] Recognized: {text}")
        except sr.UnknownValueError:
            text = ""
            print(f"[{APP_NAME}] Could not understand audio")
        except sr.RequestError as e:
            text = ""
            print(f"[{APP_NAME}] Speech recognition error: {e}")

        if text.strip() == "":
            reply = {
                "displayText": "Could not understand audio.",
                "speakText": "I could not understand. Please try again.",
                "audio_url": ""
            }
            return jsonify(reply)

        # Process query
        result = handle_query(text)
        display = result.get("displayText", "")
        speak_text = result.get("speakText", "")

        # Generate TTS audio file
        audio_url = ""
        if speak_text:
            out_name = f"reply_{unique}"
            tts_path = save_tts_mp3(speak_text, out_name)
            audio_url = f"{request.host_url.rstrip('/')}/reply_audio/{os.path.basename(tts_path)}"

        return jsonify({
            "displayText": display,
            "speakText": speak_text,
            "audio_url": audio_url
        })

    except Exception as e:
        print(f"[{APP_NAME}] upload_audio error: {e}")
        return jsonify({
            "displayText": "Server error",
            "speakText": "Server error",
            "audio_url": ""
        }), 500

@app.route("/api/browser_voice", methods=["POST"])
def api_browser_voice():
    """
    Receive audio from browser (mobile/laptop),
    convert to text, process command, return response.
    """
    try:
        if "audio" not in request.files:
            return jsonify({"displayText": "No audio file received"}), 400

        audio_file = request.files["audio"]

        # Save uploaded audio
        unique = str(uuid.uuid4())
        wav_path = os.path.join(AUDIO_DIR, f"{unique}.wav")
        audio_file.save(wav_path)

        # Speech recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="en-in")
            print(f"[{APP_NAME}] Browser voice recognized: {text}")
        except sr.UnknownValueError:
            return jsonify({
                "displayText": "Could not understand your voice",
                "speakText": "I could not understand, please try again"
            })
        except sr.RequestError as e:
            return jsonify({
                "displayText": "Speech service error",
                "speakText": "Speech recognition service failed"
            })

        # Process command
        result = handle_query(text)

        return jsonify({
            "recognizedText": text,
            "displayText": result.get("displayText", ""),
            "speakText": result.get("speakText", "")
        })

    except Exception as e:
        print(f"[{APP_NAME}] browser_voice error: {e}")
        return jsonify({
            "displayText": "Server error",
            "speakText": "Server error"
        }), 500

@app.route("/reply_audio/<path:filename>")
def serve_reply_audio(filename):
    """Serve generated TTS audio files."""
    return send_from_directory(REPLY_DIR, filename, as_attachment=False)

# ---------- CLI Mode ----------
def run_cli():
    """Run the assistant in CLI mode."""
    wish_me()
    while True:
        query = take_command().strip()
        if query:
            print(f"[{APP_NAME}] Processing: {query}")
            response = handle_query(query)
            print(f"[{APP_NAME}] {response.get('displayText', '')}")

# ---------- Main Entry Point ----------
if __name__ == "__main__":
    # Ask for mode
    print(f"=== {APP_NAME} Assistant ===")
    print("1. Voice CLI Mode")
    print("2. Web API Mode (with ESP8266 support)")
    
    mode = input("Select mode (1 or 2): ").strip()
    
    if mode == "1":
        SERVER_MODE = "cli"
        print(f"\n[{APP_NAME}] Starting in CLI mode...")
        print("Press Ctrl+C to exit\n")
        try:
            run_cli()
        except KeyboardInterrupt:
            print(f"\n[{APP_NAME}] Shutting down...")
    else:
        SERVER_MODE = "api"
        print(f"\n[{APP_NAME}] Starting API server on http://0.0.0.0:5000")
        print("ESP8266 can send audio to: POST /api/upload_audio")
        print("Browser can send audio to: POST /api/browser_voice")
        print("Web interface available at: http://localhost:5000\n")
        app.run(host="0.0.0.0", port=5000, debug=False)