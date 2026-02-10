import os

def openai_provider(message: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "AI service is configured but API key is missing."
    return f"[OpenAI ready] {message}"

def gemini_provider(message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "AI service is configured but API key is missing."
    return f"[Gemini ready] {message}"
