from fastapi import FastAPI
from chatbot import get_answer

app = FastAPI()


# 🔹 Health check endpoint (important for Docker & testing)
@app.get("/")
def root():
    return {"status": "Backend is running"}


# 🔹 Chat endpoint
@app.get("/chat")
def chat(q: str):
    response = get_answer(q)
    return {"response": response}