from fastapi import FastAPI, Request
from app.services.chatbot_service import generate_response
from app.models.schemas import ChatRequest
from app.utils.config import APP_NAME

import time
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please slow down."}
    )



app = FastAPI(title=APP_NAME)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Chatbot API"
    }


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    print(f"{request.method} {request.url} - {duration:.4f}s")
    return response

@app.post("/chat")
@limiter.limit("5/minute")
def chat(request: Request, chat_request: ChatRequest):

