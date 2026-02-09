from fastapi import FastAPI, Request
from app.services.chatbot_service import generate_response
from app.models.schemas import ChatRequest
from app.utils.config import APP_NAME
import time

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
def chat(request: ChatRequest):
    return {"response": generate_response(request.message)}
