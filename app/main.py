from fastapi import FastAPI
from app.services.chatbot_service import generate_response
from app.models.schemas import ChatRequest

app = FastAPI()
@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Chatbot API"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return generate_response(request.message)
