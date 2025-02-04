import os
from dotenv import load_dotenv

# Manually clear any old environment variables
os.environ.pop("OPENAI_API_KEY", None)

# Load environment variables from .env
load_dotenv()

# Check if the key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OpenAI API Key is missing! Check your .env file.")

# Debugging print
print("🔍 Debugging: API Key Loaded -", api_key)

