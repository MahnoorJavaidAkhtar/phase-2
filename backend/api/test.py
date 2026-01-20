"""Minimal test handler to verify Vercel serverless setup."""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create a minimal app for testing
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is working!", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy", "environment": "vercel-serverless"}

# Vercel handler
handler = app
