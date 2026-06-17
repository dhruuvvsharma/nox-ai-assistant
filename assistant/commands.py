import webbrowser
import os
import song_lib

from assistant.tts import speak
from assistant.ai import ask


def process_command(command):
    print("CLEAN COMMAND:", command)

    # 🌐 Websites
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open stackoverflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open chat gpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "open spotify" in command:
        speak("Opening Spotify")
        os.startfile("spotify:")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    # 🎵 Songs
    elif "play" in command:
        song_query = command.replace("play", "").strip().lower()

        for song in song_lib.songs:
            if song.lower() == song_query:
                speak(f"Playing {song}")
                webbrowser.open(song_lib.songs[song])
                break
        else:
            speak("Song not found")

    # 🤖 AI fallback
    else:
        speak("Let me think about that")
        ai_reply = ask(command)
        print("AI:", ai_reply)
        speak(ai_reply)