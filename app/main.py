from fastapi import FastAPI, Request
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

# -----------------------
# App setup
# -----------------------
APP_NAME = "AI Chatbot API"

app = FastAPI(title=APP_NAME)

# -----------------------
# Rate Limiter
# -----------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded. Try again later."},
    )

# -----------------------
# Request Model
# -----------------------
class ChatRequest(BaseModel):
    message: str

# -----------------------
# Health Check Endpoint
# -----------------------
@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is running"}

# -----------------------
# Chat Endpoint
# -----------------------
@app.post("/chat")
@limiter.limit("5/minute")
def chat(request: Request, chat_request: ChatRequest):
    user_message = chat_request.message

    # Temporary response (replace later with chatbot logic)
    response = f"You said: {user_message}"

    return {
        "user_input": user_message,
        "bot_response": response
    }