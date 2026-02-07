def generate_response(message: str) -> str:
    if not message or not message.strip():
        return "Please provide a valid message."
    return f"You said: {message}. This is an AI chatbot response."
