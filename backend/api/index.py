"""Vercel serverless function handler for FastAPI."""
import os

# Set environment for serverless
os.environ.setdefault("ENVIRONMENT", "production")

# Import app after setting environment
from src.main import app

# Vercel expects a variable named 'app' or 'handler'
handler = app
