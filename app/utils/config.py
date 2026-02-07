import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Chatbot")
DEBUG = os.getenv("DEBUG", "False")