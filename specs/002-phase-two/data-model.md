# Data Model: Phase II - Full-Stack Web Application

**Date**: 2026-01-18
**Feature**: Phase II - Full-Stack Web Application
**Source**: Derived from spec.md and research.md

---

## Overview

Phase II introduces two core entities: **User** and **Todo**. The data model supports multi-user authentication with user-specific todo isolation.

---

## Entity: User

### Purpose
Represents a registered user account with authentication credentials.

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique user identifier |
| `email` | String(255) | Unique, Not Null, Indexed | User's email address (used for login) |
| `password_hash` | String(255) | Not Null | Bcrypt-hashed password |
| `created_at` | DateTime | Not Null, Default: UTC now | Account creation timestamp |
| `updated_at` | DateTime | Not Null, Default: UTC now, Auto-update | Last modification timestamp |

### Validation Rules

- **Email**:
  - Must be valid email format
  - Must be unique across all users
  - Case-insensitive comparison
  - Maximum 255 characters

- **Password** (before hashing):
  - Minimum 8 characters
  - Must contain at least one letter and one number (recommended)
  - Hashed using bcrypt before storage

### Relationships

- **One-to-Many** with Todo: A user can have multiple todos
- **Cascade Delete**: When a user is deleted, all associated todos are deleted

### Indexes

- Primary index on `id`
- Unique index on `email`
- Index on `created_at` (for user analytics, if needed)

### SQLModel Implementation

```python
from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, max_length=255)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship (not stored in database)
    # todos: List["Todo"] = Relationship(back_populates="user")
```

### State Transitions

Users have no explicit state field in Phase II. Possible future states (Phase III+):
- `active` - Normal user account
- `suspended` - Temporarily disabled
- `deleted` - Soft-deleted account

---

## Entity: Todo

### Purpose
Represents a task item associated with a specific user.

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | Primary Key, Auto-increment | Unique todo identifier |
| `user_id` | Integer | Foreign Key (users.id), Not Null, Indexed | Owner of the todo |
| `title` | String(500) | Not Null | Todo title/summary |
| `description` | Text | Nullable | Optional detailed description |
| `is_complete` | Boolean | Not Null, Default: False | Completion status |
| `created_at` | DateTime | Not Null, Default: UTC now | Todo creation timestamp |
| `updated_at` | DateTime | Not Null, Default: UTC now, Auto-update | Last modification timestamp |

### Validation Rules

- **Title**:
  - Required (cannot be empty or whitespace-only)
  - Maximum 500 characters
  - Trimmed of leading/trailing whitespace

- **Description**:
  - Optional (can be null or empty)
  - No maximum length (TEXT type)

- **User ID**:
  - Must reference an existing user
  - Cannot be null
  - Foreign key constraint enforced

- **Completion Status**:
  - Boolean: `true` (complete) or `false` (incomplete)
  - Defaults to `false` on creation

### Relationships

- **Many-to-One** with User: Each todo belongs to exactly one user
- **Cascade**: When user is deleted, todos are deleted

### Indexes

- Primary index on `id`
- Foreign key index on `user_id` (for efficient user-specific queries)
- Composite index on `(user_id, created_at)` (for sorted user todo lists)
- Index on `is_complete` (for filtering by status)

### SQLModel Implementation

```python
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Todo(SQLModel, table=True):
    __tablename__ = "todos"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=500)
    description: Optional[str] = Field(default=None)
    is_complete: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship (not stored in database)
    # user: Optional[User] = Relationship(back_populates="todos")
```

### State Transitions

Todos have a simple two-state lifecycle:

```
[Created] → is_complete = False (incomplete)
    ↓
[Toggle] → is_complete = True (complete)
    ↓
[Toggle] → is_complete = False (incomplete)
    ↓
[Deleted] → Removed from database
```

**Allowed Transitions**:
- `incomplete → complete`: User marks todo as done
- `complete → incomplete`: User marks todo as not done
- `any state → deleted`: User deletes todo

---

## Relationships Diagram

```
┌─────────────────┐
│      User       │
├─────────────────┤
│ id (PK)         │
│ email (UNIQUE)  │
│ password_hash   │
│ created_at      │
│ updated_at      │
└────────┬────────┘
         │
         │ 1:N
         │
         ▼
┌─────────────────┐
│      Todo       │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │◄─── Foreign Key to User.id
│ title           │
│ description     │
│ is_complete     │
│ created_at      │
│ updated_at      │
└─────────────────┘
```

---

## Database Schema (PostgreSQL)

### Users Table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
```

### Todos Table

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    is_complete BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_todos_user_id ON todos(user_id);
CREATE INDEX idx_todos_user_created ON todos(user_id, created_at);
CREATE INDEX idx_todos_is_complete ON todos(is_complete);
```

---

## Data Integrity Rules

### User Constraints

1. **Email Uniqueness**: No two users can have the same email (case-insensitive)
2. **Password Security**: Passwords must be hashed with bcrypt before storage
3. **Cascade Delete**: Deleting a user deletes all associated todos

### Todo Constraints

1. **User Association**: Every todo must belong to an existing user
2. **Title Required**: Todo title cannot be null or empty
3. **User Isolation**: Users can only access their own todos (enforced at API level)

### Referential Integrity

- `todos.user_id` → `users.id` (Foreign Key with CASCADE DELETE)
- Database enforces referential integrity
- Application layer adds additional authorization checks

---

## Migration Strategy

### Initial Migration (Alembic)

```bash
# Create initial migration
alembic revision --autogenerate -m "Create users and todos tables"

# Apply migration
alembic upgrade head
```

### Migration File Structure

```
alembic/versions/
└── 001_create_users_and_todos_tables.py
    ├── upgrade(): Create users and todos tables with indexes
    └── downgrade(): Drop todos and users tables
```

---

## Data Access Patterns

### Common Queries

1. **Get User by Email** (for authentication):
   ```sql
   SELECT * FROM users WHERE email = ? LIMIT 1;
   ```

2. **Get All Todos for User** (sorted by creation date):
   ```sql
   SELECT * FROM todos WHERE user_id = ? ORDER BY created_at DESC;
   ```

3. **Get Incomplete Todos for User**:
   ```sql
   SELECT * FROM todos WHERE user_id = ? AND is_complete = FALSE ORDER BY created_at DESC;
   ```

4. **Update Todo Completion Status**:
   ```sql
   UPDATE todos SET is_complete = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND user_id = ?;
   ```

5. **Delete Todo** (with user authorization):
   ```sql
   DELETE FROM todos WHERE id = ? AND user_id = ?;
   ```

### Performance Considerations

- **User Lookup**: Indexed on `email` for fast authentication
- **User Todos**: Composite index on `(user_id, created_at)` for efficient sorted retrieval
- **Status Filtering**: Index on `is_complete` for filtering by completion status
- **Connection Pooling**: Use pooled connections to Neon PostgreSQL (5-10 connections)

---

## Security Considerations

### Password Storage

- **Never store plain-text passwords**
- Use bcrypt with cost factor 12 (via passlib)
- Password hash stored in `password_hash` field

### Data Isolation

- **User-Todo Isolation**: API layer enforces that users can only access their own todos
- **Authorization Checks**: Every todo operation verifies `user_id` matches authenticated user
- **SQL Injection Prevention**: Use parameterized queries (SQLModel handles this)

### Sensitive Data

- **Email**: Considered PII (Personally Identifiable Information)
- **Password Hash**: Must be protected (never exposed in API responses)
- **Todo Content**: User-private data (not shared between users in Phase II)

---

## Future Enhancements (Out of Scope for Phase II)

### User Entity Extensions
- `name` field for display name
- `email_verified` boolean for email verification
- `status` enum (active, suspended, deleted)
- `last_login_at` timestamp
- `profile_picture_url` for avatars

### Todo Entity Extensions
- `due_date` for deadlines
- `priority` enum (low, medium, high)
- `category_id` foreign key for categorization
- `tags` array or many-to-many relationship
- `parent_todo_id` for subtasks
- `position` integer for custom ordering

### Additional Entities (Phase III+)
- **Category**: Todo categories/projects
- **Tag**: Todo tags for organization
- **SharedTodo**: Collaboration between users
- **TodoHistory**: Audit trail of changes

---

## Summary

The Phase II data model consists of two entities:

1. **User**: Authentication and ownership
   - 5 fields: id, email, password_hash, created_at, updated_at
   - Unique email constraint
   - One-to-many relationship with todos

2. **Todo**: Task management
   - 7 fields: id, user_id, title, description, is_complete, created_at, updated_at
   - Foreign key to user
   - Simple complete/incomplete state

**Key Design Principles**:
- User isolation (todos are private to each user)
- Simple state management (boolean completion status)
- Referential integrity (cascade delete)
- Performance optimization (strategic indexes)
- Security (password hashing, data isolation)
