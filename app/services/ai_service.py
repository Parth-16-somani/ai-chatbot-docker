import os
from dotenv import load_dotenv
from app.services.ai_providers import openai_provider, gemini_provider

load_dotenv()

def generate_ai_response(message: str) -> str:
    provider = os.getenv("AI_PROVIDER", "openai")

    if provider == "gemini":
        return gemini_provider(message)

    return openai_provider(message)
