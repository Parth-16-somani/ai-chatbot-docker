from app.services.ai_service import generate_ai_response

def generate_response(message: str) -> dict:
    if not isinstance(message, str):
        return {
            "status": "error",
            "reply": "Message must be a string."
        }

    message = message.strip()

    if not message:
        return {
            "status": "error",
            "reply": "Please provide a valid message."
        }

    if len(message) > 200:
        return {
            "status": "error",
            "reply": "Message too long (max 200 chars)."
        }

    ai_reply = generate_ai_response(message)

    return {
        "status": "success",
        "reply": ai_reply
    }

