from fastapi import FastAPI
from app.api.documents import router as documents_router

app = FastAPI(
    title="DocFlow AI",
    description="AI-powered document assistant",
    version="0.1.0"
)

# Включваме рутера за документи с префикс /api
app.include_router(documents_router, prefix="/api")

@app.get("/")
def root():
    return {
        "message": "Welcome to DocFlow AI 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }