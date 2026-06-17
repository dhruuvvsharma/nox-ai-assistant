## NOX : "Voice AI Assistant"

NOX is a Python-based voice assistant that combines speech recognition, text-to-speech, web automation, and AI (Groq LLaMA) 
to execute voice commands and respond intelligently to user queries.



# Features
- Wake word activation ("nox")
- Voice command recognition using microphone
- Text-to-speech using Edge-TTS
- Web automation (Google, YouTube, GitHub, WhatsApp, LinkedIn, etc.)
- Music playback via YouTube links
- AI-powered responses using Groq LLM
- Modular and scalable architecture



# Tech Stack
- Python
- SpeechRecognition
- Edge-TTS
- Pygame
- Groq API (LLaMA 3)
- Webbrowser module



# Project Structure
│── main.py
│── old_nox.py
│── client.py
│── song_lib.py
│── temp_audio/
│
├── assistant/
    ├── speech.py
    ├── tts.py
    ├── commands.py
    ├── ai.py


# How to Run
1) Install dependencies: pip install speechrecognition edge-tts pygame groq
2) Run the project: python main.py


# Workflow
1) The system listens for the wake word "nox"
2) After activation, it listens for user commands
3) Commands are processed in the command handler:
4) If matched → executes action (web/music/etc.)
5) If not matched → sends request to AI model (Groq LLM)
6) Response is converted to speech using TTS engine

# Requirements
Python 3.10+
Microphone access
Active internet connection

# Future Updates:-
~This project is under active development and is evolving toward an AI powered personal assistant system.

Plugin-based command system
Memory system for conversation history
GUI interface using Flask or Streamlit
Offline speech recognition support
ML-based intent classification system

# Author
Dhruv Kandwal
B.Tech CSE (AI/DS Aspirant)


