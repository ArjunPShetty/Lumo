import speech_recognition as sr
import datetime
import webbrowser
import sys
import pywhatkit
import pyttsx3
import os
import psutil
import pyautogui
import wikipedia
from flask import Flask, request, jsonify
from flask_cors import CORS
from conv_db import get_conversational_response

APP_NAME = "LUMO"

# TTS engine (used only in CLI mode)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

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
    except Exception:
        print(f"[{APP_NAME}] Voice not working. Please type your command below:")
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

CONVERSATIONAL:
You can also chat with me! Try saying:
- Hi / Hello / Hey
- How are you?
- Tell me a joke
- I'm bored / sad / happy
- Thank you
- Goodbye
- What can you do?
- Who are you?
- And many more casual conversations!
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
        speak("No command was detected. Please try again.")
        return {"displayText": "No command detected.", "speakText": "No command was detected. Please try again."}

    # First, check for conversational responses
    chat_response = get_conversational_response(query)
    if chat_response:
        speak(chat_response)
        return {"displayText": chat_response, "speakText": chat_response}

    # Time
    if "time" in query and query.strip() == "time":
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"The time is {strTime}"
        speak(text)
        return {"displayText": text, "speakText": text}

    # Date
    if any(phrase in query for phrase in ["what day", "what date", "today's date"]):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        text = f"Today is {current_date}"
        speak(text)
        return {"displayText": text, "speakText": text}

    # Open websites
    if "open youtube" in query:
        webbrowser.open("https://youtube.com")
        text = "Opening YouTube..."
        speak(text)
        return {"displayText": text, "speakText": text}

    if "open google" in query:
        webbrowser.open("https://google.com")
        text = "Opening Google..."
        speak(text)
        return {"displayText": text, "speakText": text}

    # Play song on YouTube
    if query.startswith("play "):
        song = query.replace("play ", "", 1).strip()
        if not song:
            text = "Please specify a song to play."
            speak(text)
            return {"displayText": text, "speakText": text}
        pywhatkit.playonyt(song)
        text = f"Playing {song} on YouTube..."
        speak(text)
        return {"displayText": text, "speakText": text}

    # Google search
    if query.startswith("search "):
        search_query = query.replace("search ", "", 1).strip()
        if not search_query:
            text = "Please specify what to search."
            speak(text)
            return {"displayText": text, "speakText": text}
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        text = f"Searching Google for '{search_query}'..."
        speak(text)
        return {"displayText": text, "speakText": text}

    # Open apps (Windows)
    if query == "open notepad":
        try:
            os.startfile("notepad.exe")
            text = "Opening Notepad..."
        except Exception as e:
            text = f"Failed to open Notepad: {e}"
        speak(text)
        return {"displayText": text, "speakText": text}

    if query == "open calculator":
        try:
            os.startfile("calc.exe")
            text = "Opening Calculator..."
        except Exception as e:
            text = f"Failed to open Calculator: {e}"
        speak(text)
        return {"displayText": text, "speakText": text}

    if query == "open chrome":
        try:
            os.startfile("chrome.exe")
            text = "Opening Chrome..."
        except Exception as e:
            text = f"Failed to open Chrome: {e}"
        speak(text)
        return {"displayText": text, "speakText": text}

    # System controls (CLI only)
    if "shutdown" in query:
        if SERVER_MODE == "cli":
            speak("Shutting down your computer.")
            os.system("shutdown /s /t 1")
            return {"displayText": "System shutting down...", "speakText": "Shutting down your computer."}
        else:
            text = "Shutdown is only allowed in CLI mode."
            return {"displayText": text, "speakText": text}

    if "restart" in query:
        if SERVER_MODE == "cli":
            speak("Restarting your computer.")
            os.system("shutdown /r /t 1")
            return {"displayText": "Restarting system...", "speakText": "Restarting your computer."}
        else:
            text = "Restart is only allowed in CLI mode."
            return {"displayText": text, "speakText": text}

    if "logout" in query:
        if SERVER_MODE == "cli":
            speak("Logging out now.")
            os.system("shutdown -l")
            return {"displayText": "Logging out...", "speakText": "Logging out now."}
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
        speak(text)
        return {"displayText": text, "speakText": text}

    # Mute system volume (Windows + nircmd)
    if query == "mute":
        try:
            os.system("nircmd.exe mutesysvolume 1")
            text = "System muted."
        except Exception as e:
            text = f"Could not mute system: {e}"
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
        speak(text if SERVER_MODE == "cli" else "")
        return {"displayText": text, "speakText": text}

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
        speak(f"Searching Wikipedia for {topic}")
        summary = wikipedia.summary(topic, sentences=2, auto_suggest=False, redirect=False)
        speak(summary)
        return {"displayText": summary, "speakText": summary}
    except wikipedia.exceptions.PageError:
        text = f"Sorry, I couldn't find any page for {topic}. I will search for it on Google instead."
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        speak(text)
        return {"displayText": text, "speakText": text}
    except wikipedia.exceptions.DisambiguationError as e:
        option = e.options[0]
        summary = wikipedia.summary(option, sentences=2, auto_suggest=False, redirect=False)
        speak(summary)
        return {"displayText": summary, "speakText": summary}
    except Exception:
        text = f"Couldn't find info for {topic}, searched online."
        webbrowser.open(f"https://www.google.com/search?q={topic}")
        speak(text)
        return {"displayText": text, "speakText": text}

# ---------- Flask App ----------
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    """Serve the main HTML page"""
    from flask import send_from_directory
    return send_from_directory(".", "index.html")

@app.route("/api/command", methods=["POST"])
def api_command():
    data = request.json or {}
    query = data.get("command", "")
    result = handle_query(query)
    # Ensure the response is JSON serializable with keys frontend expects
    return jsonify({
        "displayText": result.get("displayText", ""),
        "speakText": result.get("speakText", "")
    })

# ---------- CLI Mode ----------
def run_ai():
    wish_me()
    while True:
        query = take_command().strip()
        if query:
            print(f"[{APP_NAME}] Processing: {query}")
            response = handle_query(query)
            print(f"[{APP_NAME}] {response.get('displayText','')}")


if __name__ == "__main__":
    mode = input(f"Start {APP_NAME} in (1) Voice CLI or (2) Web API mode? Enter 1 or 2: ").strip()
    if mode == "1":
        SERVER_MODE = "cli"
        run_ai()
    else:
        SERVER_MODE = "api"
        print(f"[{APP_NAME}] starting on http://127.0.0.1:5000")
        # Do not run server-side TTS when in API mode
        app.run(host="0.0.0.0", port=5000)