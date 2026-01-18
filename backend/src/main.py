"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import settings
from .api.auth import router as auth_router

# Create FastAPI app instance
app = FastAPI(
    title="Todo API - Phase II",
    description="Full-stack web application for todo management with authentication",
    version="2.0.0",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Todo API - Phase II", "version": "2.0.0"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
