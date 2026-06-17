from fileinput import filename

import speech_recognition 
import webbrowser
import edge_tts
import asyncio
import pygame
import uuid
import os
import song_lib
import time

recognizer = speech_recognition.Recognizer()


#speak function to convert text to speech
pygame.mixer.init()

def speak(text):
    print("Speaking:", text)

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    async def run():
        filename = f"voice_{uuid.uuid4().hex}.mp3"

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural"
        )

        await communicate.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        try:
            os.remove(filename)
        except:
            pass

    asyncio.run(run())

# listen_for_wake_word function to listen for the wake word "cypher"
def listen_for_wake_word():
    with speech_recognition.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=1) #noise cancellation

        while True:
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
                command = recognizer.recognize_google(audio).lower()
                if any(word in ["nox", "knox"] for word in command.split()):
                    print("Before greeting")

                    speak("Yes, how can I help you Dhruv?")
                    
                    print("After greeting")
                    return
                print(f"Heard: {command}")

                
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Speech recognition service unavailable.")
                return



def take_command():
    with speech_recognition.Microphone() as source:
        print("NOX is listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=1) #noise cancellation
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
            return recognizer.recognize_google(audio).lower()   
        
        except speech_recognition.WaitTimeoutError:
            return ""
        except speech_recognition.UnknownValueError:
            return ""
        except speech_recognition.RequestError:
            return ""
                             


from client import client
def ask(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system",
                "content": "You are Advance-Nox, you are an AI assistant. First you'll introduce yourself then give response, Give short voice assistant responses."}
                ,{"role": "user",
                "content": prompt}
                ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I am unable to connect to the AI service right now."




def process_command(command):
    print("CLEAN COMMAND:", command)
    
    if "open google" in command:
        speak("Opening Google for you Dhruv")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube for you Dhruv")
        webbrowser.open("https://www.youtube.com")
    elif "open github" in command:
        speak("Opening GitHub for you Dhruv")
        webbrowser.open("https://www.github.com")
    elif "open stackoverflow" in command:
        speak("Opening Stack Overflow for you Dhruv")
        webbrowser.open("https://stackoverflow.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn for you Dhruv")
        webbrowser.open("https://www.linkedin.com")
    elif "open chat gpt" in command:
        speak("Opening ChatGPT for you Dhruv")
        webbrowser.open("https://chat.openai.com")
    elif "open spotify" in command:
        speak("Opening Spotify for you Dhruv, Enjoy your music!")
        os.startfile("spotify:")
    elif "open google slides" in command:
        speak("Opening Google Slides for you Dhruv")
        webbrowser.open("https://www.google.com/slides")
    elif "open google docs" in command:
        speak("Opening Google Docs for you Dhruv")
        webbrowser.open("https://www.google.com/docs")
    elif "open google sheets" in command:
        speak("Opening Google Sheets for you Dhruv")
        webbrowser.open("https://www.google.com/sheets")
    elif "open DSA course" in command:
        webbrowser.open("https://www.udemy.com/course/complete-python-dsa-bootcamp/?couponCode=MT260615G2B1")
    elif "open whatsapp" in command:
        speak("Opening WhatsApp for you Dhruv")
        webbrowser.open("https://web.whatsapp.com")
    #SONGS
    elif "play" in command:
        song_query = command.replace("play", "").strip().lower()

        for song in song_lib.songs:
            if song.lower() == song_query:
                speak(f"Playing {song}")
                webbrowser.open(song_lib.songs[song])
                break
        else:
            speak("Song not found")       
    else:
        speak("Let me think about that.")

        ai_reply = ask(command)

        print("AI:", ai_reply)

        speak(ai_reply)


if __name__ == "__main__":
    speak("Initializing NOX.....")
    
    speak("Hello Dhruv,I am Noxyy")
    time.sleep(2)
    
    while True:
        listen_for_wake_word()
        command = take_command()
        if command:
            process_command(command)



  


 

