"""Authentication middleware for protected routes."""
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session, select

from ..database import get_session
from ..models import User
from ..services.auth_utils import decode_token

# HTTP Bearer token security scheme
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
) -> User:
    """Dependency to get the current authenticated user.

    Args:
        credentials: HTTP Bearer token from Authorization header
        session: Database session

    Returns:
        Authenticated User object

    Raises:
        HTTPException: If token is invalid or user not found
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode token
    token = credentials.credentials
    payload = decode_token(token)

    if payload is None:
        raise credentials_exception

    # Extract user_id from token
    user_id: Optional[int] = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    # Fetch user from database
    statement = select(User).where(User.id == int(user_id))
    user = session.exec(statement).first()

    if user is None:
        raise credentials_exception

    return user
