"""Todo API endpoints."""
from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session, select

from ..database import get_session
from ..models import Todo, User
from ..middleware.auth import get_current_user

router = APIRouter(prefix="/api/todos", tags=["Todos"])


class TodoCreate(BaseModel):
    """Request model for creating a todo."""
    title: str
    description: Optional[str] = None


class TodoUpdate(BaseModel):
    """Request model for updating a todo."""
    title: Optional[str] = None
    description: Optional[str] = None
    is_complete: Optional[bool] = None


@router.get("", response_model=List[Todo])
async def get_todos(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> List[Todo]:
    """Get all todos for the authenticated user."""
    statement = select(Todo).where(Todo.user_id == current_user.id).order_by(Todo.created_at.desc())
    todos = session.exec(statement).all()
    return list(todos)


@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_data: TodoCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Todo:
    """Create a new todo for the authenticated user."""
    new_todo = Todo(
        user_id=current_user.id,
        title=todo_data.title,
        description=todo_data.description,
        is_complete=False
    )

    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)

    return new_todo


@router.get("/{todo_id}", response_model=Todo)
async def get_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Todo:
    """Get a specific todo by ID."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    todo = session.exec(statement).first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    return todo


@router.put("/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Todo:
    """Update an existing todo."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    todo = session.exec(statement).first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.is_complete is not None:
        todo.is_complete = todo_data.is_complete

    todo.updated_at = datetime.utcnow()

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.patch("/{todo_id}", response_model=Todo)
async def patch_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Todo:
    """Partially update a todo (e.g., toggle completion status)."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    todo = session.exec(statement).first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.is_complete is not None:
        todo.is_complete = todo_data.is_complete

    todo.updated_at = datetime.utcnow()

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> None:
    """Delete a todo."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == current_user.id)
    todo = session.exec(statement).first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    session.delete(todo)
    session.commit()
