from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Resume
from app.auth import get_current_user
from app import schemas
from app.utils.skill_extractor import extract_skills

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/match", response_model=schemas.JobMatchResponse)
def match_job(
    request: schemas.JobMatchRequest, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    # 1. Fetch the LATEST resume for the CURRENT user
    resume = db.query(Resume).filter(Resume.user_id == current_user.id).order_by(Resume.id.desc()).first()
    
    if not resume:
        raise HTTPException(status_code=404, detail="No resume found. Please upload a resume first.")

    # 2. Get skills from the Resume (stored in DB as comma-separated string)
    # Example: "python, mysql, html" -> {'python', 'mysql', 'html'}
    resume_skills = set([s.strip().lower() for s in resume.skills.split(",") if s.strip()])

    # 3. Get skills from the Job Description (JD) using the fix from Step 2
    jd_skills = set(extract_skills(request.jd_text))

    if not jd_skills:
        return {
            "match_percentage": "0%",
            "matched_skills": [],
            "missing_skills": []
        }

    # 4. MATCHING LOGIC (The Intersection)
    # Only skills that are in BOTH the Resume AND the JD
    matched_skills = list(resume_skills.intersection(jd_skills))
    
    # Skills the Job wants but the user DOES NOT have
    missing_skills = list(jd_skills - resume_skills)

    # 5. ACCURATE SCORE CALCULATION
    # (Matches / Total skills the Job requested)
    match_percentage = (len(matched_skills) / len(jd_skills)) * 100

    return {
        "match_percentage": f"{round(match_percentage, 2)}%",
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }