import asyncio
import edge_tts
import os

async def speak(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save("voice.mp3")

    os.system("start voice.mp3")

asyncio.run(speak("Hello Dhruv, I am noxxy"))