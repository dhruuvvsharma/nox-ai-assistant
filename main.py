from assistant.speech import listen_for_wake_word, take_command
from assistant.commands import process_command
from assistant.tts import speak
import time

if __name__ == "__main__":
    speak("Initializing NOX.....")
    speak("Hello Dhruv, I am Noxxy")

    time.sleep(2)

    while True:
        listen_for_wake_word()
        command = take_command()

        if command:
            process_command(command)