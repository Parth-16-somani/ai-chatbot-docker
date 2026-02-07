from fastapi import FastAPI
from pydantic import BaseModel

from app.services.chatbot_service import generate_response
from app.utils.config import APP_NAME

app = FastAPI(title=APP_NAME)
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"{request.method} {request.url.path} completed in {process_time:.4f}s")

    return response

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": generate_response(request.message)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

