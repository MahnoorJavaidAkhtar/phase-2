"""Database connection configuration for Neon PostgreSQL."""
from sqlmodel import create_engine, Session
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    cors_origins: list[str] = ["http://localhost:3000"]
    environment: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Load settings
settings = Settings()

# Convert postgresql:// to postgresql+psycopg:// for psycopg3 support
database_url = settings.database_url.replace("postgresql://", "postgresql+psycopg://")

# Create SQLModel engine with connection pooling
engine = create_engine(
    database_url,
    echo=settings.environment == "development",  # Log SQL queries in dev
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=3600,  # Recycle connections after 1 hour
)


def get_session():
    """Dependency to get database session."""
    with Session(engine) as session:
        yield session
