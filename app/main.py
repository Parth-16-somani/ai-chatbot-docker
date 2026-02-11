from fastapi import FastAPI
from app.models.schemas import ChatRequest
from app.services.chatbot_service import generate_response
from app.utils.logging_config import setup_logging
import logging

# Setup centralized logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

# Health endpoint
@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Chatbot API"
    }

# Versioned chat endpoint
@app.post("/api/v1/chat")
def chat(request: ChatRequest):
    try:
        logger.info(f"Received message: {request.message}")
        return generate_response(request.message)
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            "status": "error",
            "message": "Internal server error"
        }
