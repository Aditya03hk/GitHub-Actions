from fastapi import FastAPI
from app.analyzer import count_errors

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Log Analyzer API Running"}

@app.get("/errors")
def get_error_count():
    count = count_errors("app/sample.log")

    return {
        "error_count": count
    }