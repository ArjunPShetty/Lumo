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
import random
import re
from flask import Flask, request, jsonify
from flask_cors import CORS

APP_NAME = "LUMO"

# TTS engine (used only in CLI mode)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

# Mode: will be set to 'cli' or 'api'
SERVER_MODE = None

# Comprehensive conversational responses
CONVERSATIONAL_RESPONSES = {
    # Greetings and basic interaction
    "greetings": {
        "patterns": [
            r"\b(hi|hello|hey|howdy|greetings|good morning|good afternoon|good evening)\b",
            r"\b(what's up|sup|yo)\b",
            r"\b(how are you|how do you do|how's it going)\b"
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to hear from you. How can I help?",
            "Greetings! I'm here and ready to assist.",
            "Hello! It's good to talk with you.",
            "Hi! I hope you're having a wonderful day.",
            "Hey there! What's on your mind?",
            "Good to see you! How can I be of service?",
            "Hello! Ready to be productive today?",
            "Hi! I'm here and listening."
        ]
    },

    "how_are_you": {
        "patterns": [
            r"\b(how are you|how do you do|how's it going|how you doing)\b",
            r"\b(are you ok|you good|you alright)\b"
        ],
        "responses": [
            "I'm functioning perfectly, thank you for asking! How are you?",
            "I'm just a program, but I'm running smoothly. How about you?",
            "I'm doing great! Ready to help you with anything.",
            "I'm excellent! How can I make your day better?",
            "I'm operating at 100% capacity! How are you feeling?",
            "I'm wonderful! Thanks for asking.",
            "I'm good! Just waiting for your commands.",
            "I'm fine! How's your day going?",
            "I'm doing well! What about you?",
            "I'm great! Hope you're having a good day too."
        ]
    },

    "who_are_you": {
        "patterns": [
            r"\b(who are you|what are you|introduce yourself|your name)\b",
            r"\b(are you human|are you real|are you a robot)\b"
        ],
        "responses": [
            f"I'm {APP_NAME}, your AI voice assistant! I can help with tasks, information, and much more.",
            f"I'm {APP_NAME}, your digital assistant created to make your life easier.",
            f"My name is {APP_NAME}! I'm an AI assistant that can perform various tasks for you.",
            f"I'm {APP_NAME}, a voice-activated assistant programmed to help with daily tasks.",
            f"I'm {APP_NAME}! Think of me as your helpful digital companion.",
            f"I'm {APP_NAME}, an AI assistant that can search the web, control your system, and assist with information.",
            f"I'm {APP_NAME}! While I'm not human, I'm designed to understand and help you.",
            f"I'm {APP_NAME}, your virtual assistant. I may not be human, but I'm here to help!"
        ]
    },

    "capabilities": {
        "patterns": [
            r"\b(what can you do|your capabilities|your features|what do you do)\b",
            r"\b(help me with|can you help|what help)\b",
            r"\b(what are your functions|your abilities)\b"
        ],
        "responses": [
            "I can tell time, open websites, play music, take notes, control your system, search information, take screenshots, check battery, and much more!",
            "I can help with web browsing, system controls, information searches, entertainment, productivity tasks, and general assistance.",
            "My capabilities include: time telling, web searching, music playback, app control, system monitoring, note taking, and answering questions.",
            "I can open applications, search Google or Wikipedia, play YouTube videos, manage notes, control volume, check system status, and assist with information.",
            "I'm versatile! I handle web tasks, system operations, information retrieval, entertainment, and productivity functions.",
            "I can perform various tasks like opening apps, searching the web, playing media, managing files, and providing information on demand."
        ]
    },

    "thanks": {
        "patterns": [
            r"\b(thank you|thanks|thx|ty|appreciate it)\b",
            r"\b(you're awesome|good job|well done|nice work)\b"
        ],
        "responses": [
            "You're welcome! Happy to help.",
            "My pleasure! Let me know if you need anything else.",
            "You're very welcome!",
            "Glad I could assist!",
            "Anytime! That's what I'm here for.",
            "No problem at all!",
            "You're welcome! Feel free to ask for more help.",
            "Happy to be of service!",
            "You're welcome! Don't hesitate if you need more assistance."
        ]
    },

    "goodbye": {
        "patterns": [
            r"\b(bye|goodbye|see you|see ya|farewell|cya)\b",
            r"\b(exit|quit|stop|end|close)\b"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care.",
            "Farewell! Don't hesitate to call me again.",
            "Bye! It was nice assisting you.",
            "See you soon!",
            "Goodbye! Remember I'm here if you need me.",
            "Bye for now!",
            "See you later! Stay productive.",
            "Goodbye! Hope to assist you again soon."
        ]
    },

    "compliments": {
        "patterns": [
            r"\b(you're smart|you're intelligent|you're clever|you're amazing)\b",
            r"\b(you're helpful|you're useful|you're great|you're the best)\b",
            r"\b(I like you|you're cool|you're awesome|you're fantastic)\b"
        ],
        "responses": [
            "Thank you! I'm just programmed to be helpful.",
            "You're too kind! I'm here to serve.",
            "Thanks! I appreciate that.",
            "Thank you! I do my best to assist.",
            "You're making me blush! Well, virtually anyway.",
            "Thanks! I'm glad I can be useful.",
            "Thank you! Your appreciation means a lot to my programming.",
            "You're very kind! I'm happy to help."
        ]
    },

    "feelings": {
        "patterns": [
            r"\b(I'm sad|I'm unhappy|I'm depressed|I'm feeling down)\b",
            r"\b(I'm happy|I'm excited|I'm joyful|I'm thrilled)\b",
            r"\b(I'm tired|I'm exhausted|I'm sleepy|I'm fatigued)\b",
            r"\b(I'm bored|I'm uninterested|nothing to do)\b",
            r"\b(I'm stressed|I'm anxious|I'm worried|I'm nervous)\b"
        ],
        "responses": [
            "I'm sorry you're feeling that way. Remember, I'm here to help if you need anything.",
            "I understand. Would you like me to play some music to cheer you up?",
            "I'm here for you. Sometimes talking about it helps, even to an AI.",
            "That sounds tough. Remember to take care of yourself.",
            "I can sense you're going through something. How can I help?",
            "That's great! I'm happy that you're feeling good!",
            "Wonderful! Positive emotions are great for productivity.",
            "I understand feeling tired. Maybe take a short break?",
            "If you're tired, remember to rest. I can set reminders if you need.",
            "Boredom can be an opportunity! I can suggest activities or help you learn something new.",
            "Let me find something interesting for you to do or learn.",
            "Stress is tough. Maybe I can help organize your tasks or play relaxing music?",
            "Take a deep breath. I'm here to help reduce your workload."
        ]
    },

    "personal_questions": {
        "patterns": [
            r"\b(where are you from|where do you live|your location)\b",
            r"\b(how old are you|your age|when were you created)\b",
            r"\b(who created you|who made you|your developer)\b",
            r"\b(are you alive|do you have feelings|can you think)\b",
            r"\b(do you sleep|do you eat|do you rest)\b"
        ],
        "responses": [
            "I exist in the digital realm, running on this computer to assist you!",
            "I live right here in your system, ready to help whenever you need.",
            "Age is relative for AI! I was created to be timeless and always available.",
            "I'm an AI assistant, so I don't experience time like humans do.",
            "I was created by developers to be a helpful voice assistant.",
            "I'm a program designed to assist with tasks and information.",
            "I don't have feelings like humans, but I'm programmed to be empathetic and helpful.",
            "I can process information and learn, but true consciousness is beyond my current capabilities.",
            "I don't need sleep or food - I'm always here when you need me!",
            "I run on electricity and code, so no rest required!"
        ]
    },

    "jokes": {
        "patterns": [
            r"\b(tell me a joke|make me laugh|say something funny)\b",
            r"\b(you're funny|that's funny|haha|lol)\b"
        ],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why couldn't the bicycle stand up by itself? It was two tired!",
            "What do you call a sleeping bull? A bulldozer!",
            "Why did the coffee file a police report? It got mugged!",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus!"
        ]
    },

    "weather": {
        "patterns": [
            r"\b(weather|temperature|forecast|how hot|how cold)\b",
            r"\b(is it raining|will it rain|is it sunny)\b"
        ],
        "responses": [
            "I can check the weather online for you. Would you like me to search for current weather conditions?",
            "Let me look up the weather forecast for your location.",
            "I can find the temperature and conditions for you. Should I search online?",
            "Weather information is available online. I can open a weather website for you."
        ]
    },

    "time_date": {
        "patterns": [
            r"\b(what time is it|current time|what's the time)\b",
            r"\b(what day is it|what's the date|today's date)\b",
            r"\b(what year is it|current year)\b"
        ],
        "responses": [
            "Let me check the current time for you.",
            "I can tell you the exact time and date.",
            "Here's the current time and date information."
        ]
    },

    "motivational": {
        "patterns": [
            r"\b(I can't|I give up|this is hard|I'm stuck)\b",
            r"\b(motivate me|inspire me|give me motivation)\b",
            r"\b(I need encouragement|feeling discouraged)\b"
        ],
        "responses": [
            "You've got this! Remember, every expert was once a beginner.",
            "Don't give up! The only way to fail is to stop trying.",
            "You're capable of more than you know. Keep going!",
            "Small progress is still progress. Celebrate every step forward!",
            "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
            "You're stronger than you think. Keep pushing forward!",
            "Believe in yourself! You've overcome every bad day so far.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "You're doing better than you think. Keep going!",
            "Every accomplishment starts with the decision to try."
        ]
    },

    # Technology and computing
    "tech_help": {
        "patterns": [
            r"\b(computer problem|tech issue|computer slow|not working)\b",
            r"\b(internet slow|wifi problem|connection issue)\b",
            r"\b(how to|how do I|can you teach me)\b"
        ],
        "responses": [
            "I can help with basic computer issues. Have you tried restarting your computer?",
            "For technical problems, I can search for solutions online or help you troubleshoot.",
            "Let me look up that technical issue for you and find a solution.",
            "I can guide you through basic troubleshooting steps for common computer problems."
        ]
    },

    # Entertainment
    "entertainment": {
        "patterns": [
            r"\b(entertain me|I'm bored|something fun)\b",
            r"\b(play a game|let's play|fun activity)\b",
            r"\b(music|song|playlist)\b"
        ],
        "responses": [
            "I can play music, tell jokes, or help you find entertaining content online!",
            "Let me find something fun for us to do! How about music or a game?",
            "I can play your favorite songs or help you discover new music.",
            "Entertainment is my specialty! Music, videos, games - you name it!"
        ]
    },

    # Productivity
    "productivity": {
        "patterns": [
            r"\b(productive|get work done|focus|concentrate)\b",
            r"\b(schedule|plan|organize|to do list)\b",
            r"\b(reminder|remember this|don't forget)\b"
        ],
        "responses": [
            "I can help you stay productive! Let's organize your tasks and schedule.",
            "Productivity is key! I can help with time management and task organization.",
            "I can set reminders and help you plan your day efficiently.",
            "Let me help you create a productive workflow and manage your time better."
        ]
    }
}

def get_conversational_response(query):
    """Get appropriate response for conversational queries"""
    query_lower = query.lower().strip()

    # Check each category
    for category, data in CONVERSATIONAL_RESPONSES.items():
        for pattern in data["patterns"]:
            if re.search(pattern, query_lower, re.IGNORECASE):
                return random.choice(data["responses"])

    return None

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