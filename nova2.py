# ---------------------------------------------------------
# NOVA - LLM Enhanced Voice Assistant (Groq Version)
# (Lightweight version without sentence-transformers)
# ---------------------------------------------------------

import os
import sys
import time
from datetime import datetime

import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit as pwk
import pyjokes
import wikipedia
import requests
import json

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

# Put your Groq API key in environment variable GROQ_API_KEY or hardcode here (not recommended)
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
GROQ_API_URL = "https://api.groq.com/openai/v1"

# Preferred voice index (0 or 1 on your machine). Set to 1 for Zira on Windows.
VOICE_INDEX = 1

# ---------------------------------------------------------
# TTS (pyttsx3) helpers
# ---------------------------------------------------------
def _init_engine(index: int = VOICE_INDEX):
    """Create and return a fresh pyttsx3 engine with configured voice and volume."""
    try:
        engine_local = pyttsx3.init("sapi5")
    except Exception:
        # fallback: try default init
        engine_local = pyttsx3.init()

    try:
        voices_local = engine_local.getProperty("voices")
        chosen = voices_local[index].id if len(voices_local) > index else voices_local[0].id
        engine_local.setProperty("voice", chosen)
    except Exception:
        pass
    try:
        engine_local.setProperty("volume", 1.0)
    except Exception:
        pass
    return engine_local


def speak(text: str):
    """
    Speak reliably by using a fresh TTS engine instance for each utterance.
    This avoids pyttsx3 getting stuck after microphone use on Windows.
    """
    if not text:
        return
    print("NOVA:", text)
    try:
        engine_local = _init_engine()
        engine_local.say(text)
        engine_local.runAndWait()
        try:
            engine_local.stop()
        except Exception:
            pass
    except Exception as e:
        print("TTS error:", e)


# ---------------------------------------------------------
# LIGHTWEIGHT INTENT CLASSIFIER (NO sentence-transformers)
# ---------------------------------------------------------

INTENT_KEYWORDS = {
    "open_youtube": ["open youtube", "play youtube", "start youtube"],
    "open_google": ["open google", "search google", "google search"],
    "question_answering": ["who is", "what is", "tell me about", "explain", "define"],
    "summarization": ["summarize", "summarise", "short summary"],
    "joke": ["tell me a joke", "joke", "make me laugh"],
    "play_music": ["play music", "play a song", "play on youtube"],
    "system_control": ["shutdown", "restart", "sleep"],
}


def classify_intent(query: str):
    q = (query or "").lower()

    # Direct keyword matching
    for intent, keys in INTENT_KEYWORDS.items():
        for k in keys:
            if k in q:
                return intent

    # Heuristic fallback
    if any(w in q for w in ["who", "what", "when", "where", "how", "why"]):
        return "question_answering"

    if "summary" in q or "summarize" in q:
        return "summarization"

    return "fallback"


# ---------------------------------------------------------
# LLM (GROQ) CHAT COMPLETION — robust & debug-friendly
# ---------------------------------------------------------

def groq_chat(query,
              system_prompt="Answer clearly and in a short voice-friendly way.",
              model="llama-3.1-8b-instant",
              debug=True):
    """
    Call Groq chat/completions endpoint and return the best-guess text.
    Prints raw response when debug=True for troubleshooting.
    """
    if not GROQ_API_KEY  in GROQ_API_KEY:
        # Friendly early message if key not set
        return "Groq API key not configured. Set GROQ_API_KEY environment variable."

    try:
        url = f"{GROQ_API_URL}/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}",
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
            "max_tokens": 300,
            "temperature": 0.6,
        }

        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if debug:
            print("Groq status:", resp.status_code)
            print("Groq raw response:", resp.text[:2000])  # print first 2k chars for safety

        # try to parse JSON
        data = resp.json()

        # 1) OpenAI-like structure: choices -> message -> content
        if isinstance(data, dict):
            if "choices" in data and isinstance(data["choices"], list) and len(data["choices"]) > 0:
                choice = data["choices"][0]
                # try message.content
                if isinstance(choice, dict):
                    msg = choice.get("message") or choice.get("message", {})
                    if isinstance(msg, dict) and msg.get("content"):
                        return msg["content"].strip()
                    # some providers use 'text'
                    if "text" in choice and isinstance(choice["text"], str):
                        return choice["text"].strip()
                # fallback to top-level 'text'
            # 2) top-level 'text'
            if "text" in data and isinstance(data["text"], str):
                return data["text"].strip()
            # 3) some APIs use 'result'/'output'
            for k in ("result", "output", "response"):
                if k in data:
                    v = data[k]
                    if isinstance(v, str):
                        return v.strip()
                    if isinstance(v, dict) and "content" in v:
                        return v["content"].strip()

        # final fallback: return truncated raw JSON
        return "Model returned unexpected response: " + str(data)[:1000]

    except requests.exceptions.RequestException as e:
        print("Groq network error:", e)
        return "Network error when contacting Groq."
    except ValueError as e:
        print("Groq JSON decode error:", e)
        return "Invalid response from Groq."
    except Exception as e:
        print("Groq generic error:", e)
        return "Sorry, I couldn't generate a response right now."


# ---------------------------------------------------------
# VOICE PROCESSING
# ---------------------------------------------------------

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.7)
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except Exception as e:
            print("Listen error:", e)
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query.lower()
    except Exception as e:
        print("Recognize error:", e)
        return "None"


# ---------------------------------------------------------
# ACTION HANDLER
# ---------------------------------------------------------

def handle_intent(intent, query):
    if intent == "open_youtube":
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif intent == "open_google":
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif intent == "joke":
        speak(pyjokes.get_joke())

    elif intent == "play_music":
        speak("What should I play?")
        song = take_command()
        time.sleep(0.12)  # give a tiny pause to allow audio device switch
        if song not in [None, "None"]:
            speak(f"Playing {song} on YouTube.")
            pwk.playonyt(song)

    elif intent == "system_control":
        if "shutdown" in query:
            speak("Shutting down system.")
            os.system("shutdown /s /t 5")
        elif "restart" in query:
            speak("Restarting system.")
            os.system("shutdown /r /t 5")
        elif "sleep" in query:
            speak("Putting system to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif intent == "summarization":
        speak("Here is the summary.")
        # call Groq and speak result
        ans = groq_chat(f"Summarize this: {query}")
        time.sleep(0.12)
        speak(ans)

    elif intent == "question_answering":
        speak("Let me check that.")
        ans = groq_chat(query)
        time.sleep(0.12)
        speak(ans)

    else:
        # fallback — call LLM
        ans = groq_chat(query)
        time.sleep(0.12)
        speak(ans)


# ---------------------------------------------------------
# GREETING
# ---------------------------------------------------------

def wish_me():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am NOVA. How can I help you?")


# ---------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------

if __name__ == "__main__":
    wish_me()
    time.sleep(0.5)

    while True:
        query = take_command()
        # small pause so audio device can switch back to speaker
        time.sleep(0.12)

        if query == "None":
            speak("I didn't catch that. Please repeat.")
            continue

        if any(x in query for x in ["exit", "quit", "bye", "goodbye"]):
            speak("Goodbye! Have a great day.")
            break

        # Wikipedia Shortcut
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                topic = query.replace("wikipedia", "").strip()
                result = wikipedia.summary(topic, sentences=3)
                speak("According to Wikipedia:")
                speak(result)
            except Exception as e:
                print("Wiki error:", e)
                speak("Sorry, I couldn't find anything on Wikipedia.")
            continue

        intent = classify_intent(query)
        print("Intent detected:", intent)
        handle_intent(intent, query)
