# Quickstart Guide: Phase II - Full-Stack Web Application

**Date**: 2026-01-18
**Feature**: Phase II - Full-Stack Web Application
**Purpose**: Local development setup and testing guide

---

## Prerequisites

### Required Software

- **Python**: 3.11 or higher
- **Node.js**: 18.x or higher
- **npm**: 9.x or higher (comes with Node.js)
- **Git**: For version control
- **PostgreSQL Client**: For database access (optional, for debugging)

### Required Accounts

- **Neon Account**: Sign up at https://neon.tech for serverless PostgreSQL database

---

## Project Structure

```
D:\mahnoor-kiro\
├── backend/                 # FastAPI backend
│   ├── src/
│   │   ├── models/         # SQLModel data models
│   │   ├── services/       # Business logic
│   │   ├── api/            # API routes
│   │   ├── middleware/     # Auth middleware, CORS
│   │   ├── database.py     # Database connection
│   │   └── main.py         # FastAPI app entry point
│   ├── alembic/            # Database migrations
│   ├── tests/              # Backend tests (optional)
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Environment variables (create from .env.example)
│   └── .env.example        # Environment template
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js App Router pages
│   │   ├── components/    # React components
│   │   ├── lib/           # Utilities (API client, auth)
│   │   └── types/         # TypeScript types
│   ├── public/            # Static assets
│   ├── package.json       # Node dependencies
│   ├── .env.local         # Environment variables (create from .env.local.example)
│   └── .env.local.example # Environment template
└── specs/002-phase-two/   # Design documentation
```

---

## Backend Setup

### 1. Create Neon PostgreSQL Database

1. Go to https://neon.tech and sign in
2. Create a new project: "evolution-of-todo"
3. Copy the connection string (use the **pooled connection** string)
4. Format: `postgresql://user:pass@ep-xxx-pooler.region.aws.neon.tech/neondb?sslmode=require`

### 2. Backend Environment Configuration

```bash
# Navigate to backend directory
cd backend

# Create .env file from template
cp .env.example .env
```

Edit `backend/.env`:

```env
# Database
DATABASE_URL=postgresql://user:pass@ep-xxx-pooler.region.aws.neon.tech/neondb?sslmode=require

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["http://localhost:3000"]

# Environment
ENVIRONMENT=development
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. Install Python Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt** should contain:
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlmodel==0.0.14
psycopg2-binary==2.9.9
alembic==1.13.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pydantic-settings==2.1.0
```

### 4. Initialize Database with Alembic

```bash
# Initialize Alembic (if not already done)
alembic init alembic

# Create initial migration
alembic revision --autogenerate -m "Create users and todos tables"

# Apply migration
alembic upgrade head
```

### 5. Run Backend Server

```bash
# Development mode with auto-reload
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Or using Python
python -m uvicorn src.main:app --reload
```

**Backend should be running at:** http://localhost:8000

**API Documentation:** http://localhost:8000/docs (Swagger UI)

---

## Frontend Setup

### 1. Frontend Environment Configuration

```bash
# Navigate to frontend directory
cd frontend

# Create .env.local file from template
cp .env.local.example .env.local
```

Edit `frontend/.env.local`:

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000

# Environment
NODE_ENV=development
```

### 2. Install Node Dependencies

```bash
# Install dependencies
npm install

# Or using yarn
yarn install
```

**package.json** should contain:
```json
{
  "dependencies": {
    "next": "^14.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^5.3.3"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "@types/react": "^18.2.48",
    "@types/react-dom": "^18.2.18",
    "tailwindcss": "^3.4.1",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.33",
    "eslint": "^8.56.0",
    "eslint-config-next": "^14.1.0"
  }
}
```

### 3. Run Frontend Development Server

```bash
# Development mode
npm run dev

# Or using yarn
yarn dev
```

**Frontend should be running at:** http://localhost:3000

---

## Verification Steps

### 1. Backend Health Check

```bash
# Test backend is running
curl http://localhost:8000/

# Expected response: {"message": "Todo API - Phase II"}
```

### 2. Database Connection Check

```bash
# Test database connectivity (if health endpoint exists)
curl http://localhost:8000/health/db

# Expected response: {"status": "healthy", "database": "connected"}
```

### 3. API Documentation

Open browser: http://localhost:8000/docs

You should see Swagger UI with:
- Authentication endpoints (`/auth/signup`, `/auth/token`, `/auth/logout`)
- Todo endpoints (`/api/todos`, `/api/todos/{id}`)

### 4. Frontend Access

Open browser: http://localhost:3000

You should see the Next.js application homepage.

---

## Testing the Application

### Manual Testing Flow

#### 1. User Signup

```bash
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123"
  }'
```

**Expected Response:**
```json
{
  "message": "User created successfully",
  "user_id": 1
}
```

#### 2. User Login

```bash
curl -X POST http://localhost:8000/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=SecurePass123"
```

**Expected Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

**Save the access_token for subsequent requests.**

#### 3. Create Todo

```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread"
  }'
```

**Expected Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_complete": false,
  "created_at": "2026-01-18T10:30:00Z",
  "updated_at": "2026-01-18T10:30:00Z"
}
```

#### 4. Get All Todos

```bash
curl -X GET http://localhost:8000/api/todos \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "is_complete": false,
    "created_at": "2026-01-18T10:30:00Z",
    "updated_at": "2026-01-18T10:30:00Z"
  }
]
```

#### 5. Toggle Todo Completion

```bash
curl -X POST http://localhost:8000/api/todos/1/toggle \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_complete": true,
  "created_at": "2026-01-18T10:30:00Z",
  "updated_at": "2026-01-18T10:30:00Z"
}
```

#### 6. Delete Todo

```bash
curl -X DELETE http://localhost:8000/api/todos/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response:** HTTP 204 No Content

---

## Frontend Testing

### 1. Navigate to Signup Page

Open: http://localhost:3000/signup

- Enter email and password
- Click "Sign Up"
- Should redirect to signin page or todos page

### 2. Navigate to Signin Page

Open: http://localhost:3000/signin

- Enter email and password
- Click "Sign In"
- Should redirect to todos page

### 3. Todo Management

Open: http://localhost:3000/todos

- View list of todos
- Click "Add Todo" to create new todo
- Click checkbox to toggle completion
- Click "Edit" to modify todo
- Click "Delete" to remove todo

### 4. Responsive Design Test

- Resize browser window to mobile size (320px width)
- Verify UI adapts and remains usable
- Test on actual mobile device if available

---

## Troubleshooting

### Backend Issues

**Problem:** `ModuleNotFoundError: No module named 'fastapi'`
- **Solution:** Activate virtual environment and run `pip install -r requirements.txt`

**Problem:** `sqlalchemy.exc.OperationalError: could not connect to server`
- **Solution:** Check DATABASE_URL in `.env` file, verify Neon database is accessible

**Problem:** `alembic.util.exc.CommandError: Can't locate revision identified by`
- **Solution:** Delete `alembic/versions/*.py` and run `alembic revision --autogenerate` again

**Problem:** `401 Unauthorized` on protected endpoints
- **Solution:** Ensure Authorization header includes valid JWT token: `Bearer <token>`

### Frontend Issues

**Problem:** `Error: ECONNREFUSED` when calling API
- **Solution:** Verify backend is running on http://localhost:8000

**Problem:** CORS errors in browser console
- **Solution:** Check CORS_ORIGINS in backend `.env` includes `http://localhost:3000`

**Problem:** `Module not found` errors
- **Solution:** Run `npm install` to install dependencies

**Problem:** Environment variables not loading
- **Solution:** Restart Next.js dev server after changing `.env.local`

### Database Issues

**Problem:** Migration fails with "relation already exists"
- **Solution:** Drop all tables and rerun migrations, or use `alembic stamp head` to mark as applied

**Problem:** Connection pool exhausted
- **Solution:** Reduce `DB_POOL_SIZE` in `.env` or check for connection leaks

---

## Development Workflow

### Daily Development

1. **Start Backend:**
   ```bash
   cd backend
   venv\Scripts\activate  # Windows
   uvicorn src.main:app --reload
   ```

2. **Start Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Make Changes:**
   - Edit code in `backend/src/` or `frontend/src/`
   - Changes auto-reload in development mode

4. **Test Changes:**
   - Use Swagger UI: http://localhost:8000/docs
   - Use Frontend: http://localhost:3000
   - Use curl commands for API testing

### Database Schema Changes

1. **Modify SQLModel models** in `backend/src/models/`
2. **Create migration:**
   ```bash
   alembic revision --autogenerate -m "Description of change"
   ```
3. **Review migration** in `alembic/versions/`
4. **Apply migration:**
   ```bash
   alembic upgrade head
   ```
5. **Test rollback:**
   ```bash
   alembic downgrade -1
   alembic upgrade head
   ```

### Adding New API Endpoints

1. **Update contract** in `specs/002-phase-two/contracts/`
2. **Implement route** in `backend/src/api/`
3. **Test with Swagger UI** or curl
4. **Update frontend API client** in `frontend/src/lib/api-client.ts`
5. **Implement UI** in `frontend/src/`

---

## Production Deployment (Future)

### Backend Deployment

- Deploy to cloud platform (AWS, Azure, GCP, Heroku, Railway, etc.)
- Set environment variables in platform dashboard
- Use production DATABASE_URL from Neon
- Set `ENVIRONMENT=production`
- Enable HTTPS
- Configure production CORS_ORIGINS

### Frontend Deployment

- Deploy to Vercel, Netlify, or similar
- Set `NEXT_PUBLIC_API_URL` to production backend URL
- Configure environment variables in platform dashboard
- Enable HTTPS

### Database

- Use Neon production branch
- Enable connection pooling
- Set up automated backups
- Monitor connection usage

---

## Useful Commands

### Backend

```bash
# Run backend
uvicorn src.main:app --reload

# Run with specific host/port
uvicorn src.main:app --host 0.0.0.0 --port 8000

# Create migration
alembic revision --autogenerate -m "message"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# Check current migration version
alembic current

# View migration history
alembic history
```

### Frontend

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint

# Type check
npx tsc --noEmit
```

### Database

```bash
# Connect to Neon database (using psql)
psql "postgresql://user:pass@host/db?sslmode=require"

# List tables
\dt

# Describe table
\d users
\d todos

# Query data
SELECT * FROM users;
SELECT * FROM todos WHERE user_id = 1;
```

---

## Next Steps

After completing local setup:

1. **Review API Documentation:** http://localhost:8000/docs
2. **Test all user stories** from spec.md
3. **Verify data isolation** (create multiple users, ensure todos are private)
4. **Test responsive design** on mobile devices
5. **Review code quality** (linting, type checking)
6. **Prepare for Phase III** (advanced features)

---

## Support

- **API Documentation:** http://localhost:8000/docs
- **Spec Document:** `specs/002-phase-two/spec.md`
- **Data Model:** `specs/002-phase-two/data-model.md`
- **API Contracts:** `specs/002-phase-two/contracts/`
- **Research Notes:** `specs/002-phase-two/research.md`
