The goal behind NOVA was to build an AI assistant capable of performing various computer operations hands-free—ranging from opening applications to fetching data online. 
By integrating speech recognition, text-to-speech, and multiple automation libraries, NOVA becomes a proactive tool that listens, understands, and executes commands in real-time.

Key Features:
1)Voice Recognition & Response: NOVA listens using a microphone and understands commands via Google's speech recognition engine. It responds using pyttsx3, providing clear audio feedback.
2)Time-Based Greetings: Depending on the time of day, NOVA greets the user with a personalized message and introduces itself as “Mister Nobody.”
3)Web Automation: NOVA can open popular websites like YouTube, Google, Stack Overflow, LinkedIn, and Facebook. For Google, it asks for a search term and executes the query dynamically.
4)Wikipedia Integration: Users can ask NOVA to summarize topics using the wikipedia module, which returns concise results from Wikipedia.
5)Media Control: NOVA can play songs from a specified music directory and even stream content directly on YouTube based on user input.
6)System Operations: It supports system-level operations like opening Notepad, VS Code, Command Prompt, and even initiating shutdown, restart, or sleep modes.
7)Fun Add-ons: NOVA can crack jokes using the pyjokes library and share the system’s IP address via the requests module.

Technical Stack:
1)Languages & Libraries: Python, speech_recognition, pyttsx3, wikipedia, webbrowser, os, cv2, requests, pywhatkit, pyjokes
2)System Integration: Uses os.startfile() and webbrowser.open() for local and web automation
3)Hardware Requirement: Microphone for voice input and speaker/headphones for audio output

NOVA serves as an efficient, hands-free assistant built entirely using Python. 
It reflects my growing interest in AI, automation, and voice technology, and demonstrates how software can simplify everyday computer usage.
This project not only deepened my technical knowledge but also taught me valuable lessons in system design, error handling, and user experience.
