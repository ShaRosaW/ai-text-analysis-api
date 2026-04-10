import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")