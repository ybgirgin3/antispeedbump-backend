from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()
origins = ["*"]


@api.get("/")
def home():
    return {
        "Greetings": "Welcome to the Antispeedbump, you can save and share your instagram post",
    }
