from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import engine, Base
from app.routes import users, resumes, jobs
import os

# 1. Database Initialization
# Ye line aapke models ke hisaab se tables create karegi
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resume Analyzer API")

# 2. CORS Middleware
# Isse aapka frontend backend se asani se communicate kar payega
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. API Routers
# Aapke existing routes yahan include ho rahe hain
app.include_router(users.router)
app.include_router(resumes.router)
app.include_router(jobs.router)

# --- START: FRONTEND & STATIC FILES INTEGRATION ---

# Aapke folder ka naam 'fronted' hai (as per screenshot)
FRONTEND_DIR = "fronted"

# Check karein ki folder exist karta hai ya nahi
if os.path.exists(FRONTEND_DIR):
    # Static files (CSS, JS, Images) ko serve karne ke liye mount karein
    app.mount("/fronted", StaticFiles(directory=FRONTEND_DIR), name="fronted")

# Root URL (http://localhost:8000/) par index.html dikhane ke liye
@app.get("/")
async def serve_frontend():
    index_file = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"error": f"index.html not found in {FRONTEND_DIR} folder"}

# --- END: FRONTEND INTEGRATION ---

if __name__ == "__main__":
    import uvicorn
    # Render default port 10000 use karta hai, local par 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)