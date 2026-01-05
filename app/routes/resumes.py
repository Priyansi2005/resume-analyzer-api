from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Resume
from app.auth import get_current_user
from app.utils.resume_parser import parse_resume
from app.utils.skill_extractor import extract_skills
from app.utils.resume_scorer import calculate_score
import shutil, os

router = APIRouter(prefix="/resumes", tags=["Resumes"])

@router.post("/upload")
def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process resume
    raw_text = parse_resume(file_path)
    found_skills = extract_skills(raw_text)
    score = calculate_score(found_skills, experience_years=2)

    # Save to DB
    new_resume = Resume(
        filename=file.filename,
        content=raw_text,
        skills=", ".join(found_skills),
        score=score,
        user_id=current_user.id
    )
    db.add(new_resume)
    db.commit()

    # Clean Response (Matches your image!)
    return {
        "filename": file.filename,
        "score": score,
        "skills": found_skills
    }