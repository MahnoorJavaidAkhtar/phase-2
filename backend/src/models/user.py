"""User model for authentication and ownership."""
from __future__ import annotations

from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """User account with authentication credentials."""

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, max_length=255)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
