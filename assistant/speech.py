import speech_recognition

from assistant.tts import speak 

recognizer = speech_recognition.Recognizer()

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
                       