from fastapi import FastAPI
from pydantic import BaseModel

from app.services.chatbot_service import generate_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": generate_response(request.message)}
