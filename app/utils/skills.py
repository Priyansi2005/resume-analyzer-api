from fastapi import APIRouter, Depends
from app import schemas

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/match", response_model=schemas.JobMatchResponse)
def match_job(request: schemas.JobMatchRequest):
    # This is a simple matching logic for testing
    jd_text = request.jd_text.lower()
    
    # Example: List of skills we are looking for in the JD
    required_skills = ["python", "html", "css", "mysql", "figma"]
    matched = [skill for skill in required_skills if skill in jd_text]
    
    match_percentage = (len(matched) / len(required_skills)) * 100
    
    return {
        "match_percentage": f"{match_percentage}%",
        "matched_skills": matched
    }# app/utils/skills.py

# Ensure this name is exactly SKILLS_DB
SKILLS_DB = [
    # --- TECHNICAL SKILLS (From Rajan's Resume) ---
    "html", "css", "figma", "video editing", "python", "mysql", "odoo",
    "cloud", "networking", "computer assemble", "product development",
    "system integration", "android", "kotlin", "linux", "image processing",
    "ml algorithms", "iot", "ai", "artificial intelligence", "machine learning",

    # --- SOFT SKILLS (From Rajan's Resume) ---
    "communication", "leadership", "problem solving", "time management",
    "creativity", "quick learner", "teamwork", "dedicated",

    # --- WEB DEVELOPMENT & DESIGN ---
    "javascript", "typescript", "react", "angular", "vue", "next.js", "node.js", 
    "fastapi", "flask", "django", "php", "laravel", "tailwind", "bootstrap",
    "ux design", "ui design", "adobe xd", "photoshop", "illustrator",

    # --- BACKEND & DATABASE ---
    "sql", "postgresql", "mongodb", "redis", "firebase", "sqlite", "oracle",
    "rest api", "graphql", "microservices", "docker", "kubernetes",

    # --- DATA SCIENCE & AI ---
    "data analysis", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "deep learning", "nlp", "tableau", "power bi", "r", "matlab",

    # --- MOBILE & PROGRAMMING LANGUAGES ---
    "java", "c++", "c#", "swift", "flutter", "react native", "go", "rust", "ruby",

    # --- DEVOPS & CLOUD ---
    "aws", "azure", "gcp", "git", "github", "gitlab", "jenkins", "cicd", 
    "terraform", "ansible", "linux administration",

    # --- BUSINESS & MANAGEMENT ---
    "project management", "agile", "scrum", "sdlc", "analytical skills", 
    "critical thinking", "negotiation", "public speaking", "strategic planning"
]