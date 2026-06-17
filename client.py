from dotenv import load_dotenv
import dotenv
from groq import Groq
import os

dotenv.load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(os.getenv("GROQ_API_KEY"))

client = Groq(api_key=GROQ_API_KEY)