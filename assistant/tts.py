from fileinput import filename

import speech_recognition 
import edge_tts
import asyncio
import pygame
import uuid
import os

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