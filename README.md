NOVA — LLM-Enhanced Voice Assistant
A Python-based voice assistant powered by Groq LLMs, SpeechRecognition & automation

🚀 Overview
NOVA is an intelligent, hands-free AI assistant built using Python.
It listens to your voice, understands your intent, performs system tasks, and generates intelligent responses using Groq LLM models such as llama-3.1-8b-instant.

NOVA combines:
Voice recognition
Text-to-speech
Web & system automation
Large language model reasoning

This project demonstrates real-time voice interaction combined with GenAI capabilities.

✨ Features
Voice Recognition & TTS
Listens using speech_recognition (Google STT).
Speaks naturally using pyttsx3 (SAPI5).
LLM-Powered Intelligence (Groq API)
Answers open-ended questions
Explains concepts
Summarizes content
Acts as a fallback when commands are unclear
Smart Intent Detection (Lightweight)

Detects commands like:
Opening apps
Playing music
Asking questions
Summarization
Web search
System controls

🌐 Web Automation

Open Google, YouTube, LinkedIn, Facebook, Stack Overflow
Dynamic Google search (“What should I search?”)

📚 Wikipedia Integration

Ask: “Tell me about quantum computing”

NOVA fetches & speaks a concise summary

🎵 Media Controls
Plays local audio
Plays YouTube videos via pywhatkit

🖥️ System Automation
Open Notepad, VS Code, Command Prompt
Shutdown, restart, sleep

🧰 Tech Stack
Core
Python 3.10–3.12 (Windows)
SpeechRecognition
pyttsx3 (SAPI5)
requests
pywhatkit
pyjokes
wikipedia
AI / LLM
Groq API
llama-3.1-8b-instant (recommended)
Optional: embeddings (sentence-transformers) for advanced intent detection

System
Windows (preferred)
Microphone + speakers

📦 Installation
1. Clone the repository
git clone https://github.com/yourusername/NOVA-Voice-Assistant.git
cd NOVA-Voice-Assistant

2. Create & activate a virtual environment
python -m venv novaenv
.\novaenv\Scripts\Activate.ps1
pip install --upgrade pip

3. Install dependencies
pip install pyttsx3 SpeechRecognition requests pywhatkit pyjokes wikipedia pipwin
pipwin install pyaudio   # Microphone support

(If you later want embeddings-based intent detection, install torch + sentence-transformers.)

4. Set your Groq API Key
In PowerShell:
setx GROQ_API_KEY "gsk_your_key_here"
Close & reopen PowerShell, then activate novaenv again.

▶️ Running NOVA
python nova2.py

Say commands like:
“Open YouTube”
“Tell me a joke”
“What is machine learning?”
“Summarize the Indian Constitution”
“Search on Google”
“Exit”

NOVA will listen → understand → act → respond with speech.

🧪 Example Conversation
You:
What is Python?
NOVA:
Python is a high-level programming language known for its simplicity…

⚠️ Troubleshooting
❌ No sound / silent responses
Open Volume Mixer and ensure python.exe is not muted
Try switching VOICE_INDEX in the script (0 or 1)

Test TTS:
python -c "import pyttsx3; e=pyttsx3.init('sapi5'); e.say('hello'); e.runAndWait()"
❌ Groq returns “Invalid API Key”
Recreate the key in Groq Console
Ensure no extra quotes/spaces:
python -c "import os; print(repr(os.getenv('GROQ_API_KEY')))"

❌ Model Decommissioned Error
Update model in groq_chat():
model="llama-3.1-8b-instant"

🏗️ Project Structure
NOVA/
│
├── nova2.py                # Main voice assistant
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

🔮 Future Enhancements

Wake-word activation (“Hey Nova”)
Embeddings-based intent detection
Browser extension for cloud-based NOVA
FastAPI server for remote control
Realtime TTS streaming
RAG with Qdrant for document answering

✍️ Author
Vedant Deepak Malpure
