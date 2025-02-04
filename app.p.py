import os
from dotenv import load_dotenv

os.environ.pop("OPENAI_API_KEY", None)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OpenAI API Key is missing! Check your .env file.")

print("🔍 Debugging: API Key Loaded -", api_key)

