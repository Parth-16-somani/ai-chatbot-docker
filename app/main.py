from fastapi import FastAPI
from app.services.chatbot_service import generate_response
from app.models.schemas import ChatRequest

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": generate_response(request.message)}
