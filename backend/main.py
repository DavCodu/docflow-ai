from fastapi import FastAPI

app = FastAPI(
    title="DocFlow AI API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to DocFlow AI 🚀"
    }