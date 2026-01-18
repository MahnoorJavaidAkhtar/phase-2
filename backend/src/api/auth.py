"""Authentication API endpoints."""
from datetime import timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from sqlmodel import Session, select

from ..database import get_session, settings
from ..models import User
from ..services.auth_utils import hash_password, verify_password, create_access_token
from ..middleware.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


# Request/Response models
class SignupRequest(BaseModel):
    """User signup request."""
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    """User signup response."""
    message: str
    user_id: int


class TokenResponse(BaseModel):
    """Token response."""
    access_token: str
    token_type: str
    expires_in: int


class UserResponse(BaseModel):
    """User response (no password)."""
    id: int
    email: str
    created_at: str


class MessageResponse(BaseModel):
    """Generic message response."""
    message: str


@router.post("/signup", response_model=SignupResponse, status_code=status.HTTP_201_CREATED)
async def signup(
    signup_data: SignupRequest,
    session: Session = Depends(get_session)
):
    """Register a new user.

    Args:
        signup_data: Email and password
        session: Database session

    Returns:
        Success message with user ID

    Raises:
        HTTPException: If email already exists or validation fails
    """
    # Check if email already exists
    statement = select(User).where(User.email == signup_data.email)
    existing_user = session.exec(statement).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Validate password length
    if len(signup_data.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters"
        )

    # Create new user
    hashed_password = hash_password(signup_data.password)
    new_user = User(
        email=signup_data.email,
        password_hash=hashed_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return SignupResponse(
        message="User created successfully",
        user_id=new_user.id
    )


@router.post("/token", response_model=TokenResponse)
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    """User login - returns JWT token.

    Args:
        response: FastAPI response object (for setting cookies)
        form_data: OAuth2 form with username (email) and password
        session: Database session

    Returns:
        JWT access token

    Raises:
        HTTPException: If credentials are invalid
    """
    # Find user by email (username field contains email)
    statement = select(User).where(User.email == form_data.username)
    user = session.exec(statement).first()

    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires
    )

    # Set HTTP-only cookie
    response.set_cookie(
        key="auth_token",
        value=access_token,
        httponly=True,
        secure=settings.environment == "production",
        samesite="lax",
        max_age=settings.access_token_expire_minutes * 60
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.access_token_expire_minutes * 60
    )


@router.post("/logout", response_model=MessageResponse)
async def logout(
    response: Response,
    current_user: User = Depends(get_current_user)
):
    """User logout - clears auth cookie.

    Args:
        response: FastAPI response object (for clearing cookies)
        current_user: Authenticated user from dependency

    Returns:
        Success message
    """
    # Clear auth cookie
    response.delete_cookie(key="auth_token")

    return MessageResponse(message="Logged out successfully")


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    """Get current authenticated user information.

    Args:
        current_user: Authenticated user from dependency

    Returns:
        User information (without password)
    """
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        created_at=current_user.created_at.isoformat()
    )
