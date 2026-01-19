# 🚀 Deployment Guide - Todo Application

This guide covers deploying your full-stack todo application with Next.js frontend and FastAPI backend.

## 📋 Table of Contents
- [Architecture Overview](#architecture-overview)
- [Prerequisites](#prerequisites)
- [Backend Deployment](#backend-deployment)
- [Frontend Deployment](#frontend-deployment)
- [Environment Variables](#environment-variables)
- [Post-Deployment](#post-deployment)

---

## 🏗️ Architecture Overview

**Tech Stack:**
- **Frontend**: Next.js 14 (React, TypeScript, Tailwind CSS)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (Neon - already configured)

**Deployment Strategy:**
- Frontend → Vercel (optimized for Next.js)
- Backend → Railway/Render/Heroku
- Database → Neon (already cloud-hosted)

---

## ✅ Prerequisites

Before deploying, ensure you have:
- [x] GitHub repository with latest code
- [x] Neon database (already configured)
- [x] Accounts on deployment platforms:
  - Vercel account (https://vercel.com)
  - Railway/Render account (choose one)

---

## 🔧 Backend Deployment

### Option 1: Railway (Recommended)

**Why Railway?**
- Free tier available
- Automatic deployments from GitHub
- Built-in PostgreSQL support5
- Simple environment variable management

**Steps:**

1. **Sign up at Railway**
   - Go to https://railway.app
   - Sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `MahnoorJavaidAkhtar/phase-2`

3. **Configure Service**
   - Railway will detect Python automatically
   - Set root directory: `backend`
   - Railway will use your `Procfile` automatically

4. **Add Environment Variables**
   ```
   DATABASE_URL=postgresql://neondb_owner:npg_tqX2eKyQiGb7@ep-raspy-wind-ahm4fh0h-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
   SECRET_KEY=Z-5t-Vlpwci_AlAWzM5H913EDrv0cMbnYUAGc_h9rIs
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   CORS_ORIGINS=["https://your-frontend-url.vercel.app"]
   ENVIRONMENT=production
   ```

5. **Deploy**
   - Click "Deploy"
   - Railway will build and deploy automatically
   - Copy your backend URL (e.g., `https://your-app.railway.app`)

---

### Option 2: Render

**Steps:**

1. **Sign up at Render**
   - Go to https://render.com
   - Sign in with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `MahnoorJavaidAkhtar/phase-2`

3. **Configure Service**
   ```
   Name: todo-backend
   Region: Choose closest to you
   Branch: 002-phase-two
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn src.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Add Environment Variables**
   - Same as Railway (see above)
   - Update `CORS_ORIGINS` with your Vercel URL

5. **Deploy**
   - Click "Create Web Service"
   - Copy your backend URL

---

### Option 3: Heroku

**Steps:**

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and Create App**
   ```bash
   heroku login
   cd backend
   heroku create your-todo-backend
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set DATABASE_URL="your-neon-url"
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set CORS_ORIGINS='["https://your-frontend.vercel.app"]'
   ```

4. **Deploy**
   ```bash
   git subtree push --prefix backend heroku main
   ```

---

## 🎨 Frontend Deployment

### Vercel (Recommended for Next.js)

**Steps:**

1. **Sign up at Vercel**
   - Go to https://vercel.com
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Import `MahnoorJavaidAkhtar/phase-2`

3. **Configure Project**
   ```
   Framework Preset: Next.js
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: .next
   Install Command: npm install
   ```

4. **Add Environment Variables**
   - Go to "Settings" → "Environment Variables"
   - Add:
     ```
     NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
     NODE_ENV=production
     ```

5. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy automatically
   - Your app will be live at `https://your-app.vercel.app`

6. **Update Backend CORS**
   - Go back to your backend deployment (Railway/Render)
   - Update `CORS_ORIGINS` environment variable:
     ```
     CORS_ORIGINS=["https://your-app.vercel.app"]
     ```
   - Redeploy backend

---

## 🔐 Environment Variables

### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:pass@host/db?sslmode=require

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS - UPDATE WITH YOUR VERCEL URL
CORS_ORIGINS=["https://your-frontend.vercel.app"]

# Environment
ENVIRONMENT=production
```

### Frontend (.env.local)
```env
# API Configuration - UPDATE WITH YOUR BACKEND URL
NEXT_PUBLIC_API_URL=https://your-backend.railway.app

# Environment
NODE_ENV=production
```

---

## 🔄 Post-Deployment

### 1. Test Your Deployment

**Backend Health Check:**
```bash
curl https://your-backend-url.railway.app/docs
```
Should return the FastAPI documentation page.

**Frontend Check:**
- Visit `https://your-app.vercel.app`
- Try signing up
- Create a todo
- Verify all features work

### 2. Run Database Migrations

If you have pending migrations:
```bash
# SSH into your backend service or run locally
alembic upgrade head
```

### 3. Monitor Logs

**Railway:**
- Go to your project → Click on service → View logs

**Vercel:**
- Go to your project → Click on deployment → View function logs

### 4. Set Up Custom Domain (Optional)

**Vercel:**
- Go to Settings → Domains
- Add your custom domain
- Update DNS records as instructed

**Railway:**
- Go to Settings → Domains
- Add custom domain
- Update DNS records

### 5. Enable Automatic Deployments

Both Vercel and Railway support automatic deployments:
- Every push to `002-phase-two` branch will trigger a new deployment
- Preview deployments for pull requests

---

## 🐛 Troubleshooting

### CORS Errors
**Problem:** Frontend can't connect to backend

**Solution:**
1. Check backend `CORS_ORIGINS` includes your Vercel URL
2. Ensure URL has no trailing slash
3. Redeploy backend after changing CORS settings

### Database Connection Issues
**Problem:** Backend can't connect to Neon database

**Solution:**
1. Verify `DATABASE_URL` is correct
2. Check Neon database is active
3. Ensure `sslmode=require` is in connection string

### Build Failures
**Problem:** Deployment fails during build

**Solution:**
1. Check build logs for specific errors
2. Verify all dependencies are in `requirements.txt` / `package.json`
3. Test build locally first:
   ```bash
   # Frontend
   cd frontend && npm run build

   # Backend
   cd backend && pip install -r requirements.txt
   ```

### Environment Variables Not Working
**Problem:** App can't read environment variables

**Solution:**
1. Verify variables are set in deployment platform
2. For frontend, ensure variables start with `NEXT_PUBLIC_`
3. Redeploy after adding/changing variables

---

## 📊 Monitoring & Maintenance

### Performance Monitoring
- **Vercel Analytics**: Enable in project settings
- **Railway Metrics**: View CPU, memory, network usage

### Database Backups
- Neon provides automatic backups
- Check Neon dashboard for backup settings

### Security Updates
- Regularly update dependencies:
  ```bash
  # Frontend
  npm update

  # Backend
  pip list --outdated
  pip install --upgrade package-name
  ```

---

## 🎉 Success Checklist

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] Database connected successfully
- [ ] CORS configured correctly
- [ ] Environment variables set
- [ ] Sign up/Sign in working
- [ ] Todo CRUD operations working
- [ ] Automatic deployments enabled
- [ ] Custom domain configured (optional)
- [ ] Monitoring set up

---

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [Render Documentation](https://render.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Next.js Deployment](https://nextjs.org/docs/deployment)
- [Neon Documentation](https://neon.tech/docs)

---

## 🆘 Need Help?

If you encounter issues:
1. Check deployment platform logs
2. Review this guide's troubleshooting section
3. Check GitHub Issues for similar problems
4. Contact platform support (Vercel, Railway, etc.)

---

**Happy Deploying! 🚀**
