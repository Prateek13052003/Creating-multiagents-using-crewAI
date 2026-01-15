from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # MUST be before getenv

print("KEY FOUND:", bool(os.getenv("GROQ_API_KEY")))  # debug

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()
for model in models.data:
    print(model.id)
