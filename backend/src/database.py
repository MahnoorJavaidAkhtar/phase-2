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

# Create SQLModel engine with serverless-friendly settings
# Use minimal pooling for serverless environments
is_serverless = settings.environment == "production"
engine = create_engine(
    database_url,
    echo=settings.environment == "development",  # Log SQL queries in dev
    pool_size=1 if is_serverless else 5,  # Minimal pool for serverless
    max_overflow=0 if is_serverless else 10,  # No overflow for serverless
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=300 if is_serverless else 3600,  # Shorter recycle for serverless
    connect_args={
        "connect_timeout": 10,  # 10 second timeout
        "options": "-c statement_timeout=30000"  # 30 second query timeout
    }
)


def get_session():
    """Dependency to get database session."""
    with Session(engine) as session:
        yield session
