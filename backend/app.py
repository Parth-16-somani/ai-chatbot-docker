from fastapi import FastAPI
from chatbot import get_answer

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Chatbot running"}


@app.get("/chat")
def chat(q: str):
    return {"response": get_answer(q)}