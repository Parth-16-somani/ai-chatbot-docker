from app.services.ai_service import generate_ai_response

def generate_response(message: str) -> dict:
    if not isinstance(message, str):
       return {
    "status": "success",
    "data": {
        "user_message": message,
        "ai_reply": ai_reply
    }
}


    message = message.strip()

    if not message:
       return {
    "status": "error",
    "message": "Error message here"
}

    if len(message) > 200:
        return {
    "status": "error",
    "message": "Error message here"
}

    ai_reply = generate_ai_response(message)

    return {
        "status": "success",
        "reply": ai_reply
    }
