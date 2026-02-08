def generate_response(message: str) -> dict:
    if not message or not message.strip():
        return {
            "status": "error",
            "reply": "Please provide a valid message."
        }

    return {
        "status": "success",
        "reply": f"You said: {message}. This is an AI chatbot response."
    }
