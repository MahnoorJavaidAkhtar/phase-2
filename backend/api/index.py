"""Vercel serverless function handler for FastAPI."""
from src.main import app

# Vercel expects a variable named 'app' or 'handler'
handler = app
