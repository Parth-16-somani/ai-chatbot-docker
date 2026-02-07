from app.utils.redis_client import redis_client

def generate_response(message: str) -> str:

    cached_response = redis_client.get(message)
    if cached_response:
        return cached_response

    response = f"You said: {message}. This is an AI chatbot response."

    redis_client.set(message, response)

    return response
