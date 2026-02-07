from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Docker Compose project running 🚀",
        "db_host": os.getenv("DB_HOST")
    }
