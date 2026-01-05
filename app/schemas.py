from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ---------- USER SCHEMAS ----------

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True # Allows Pydantic to read from SQLAlchemy models

# ---------- TOKEN SCHEMAS ----------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# ---------- RESUME SCHEMAS ----------

class ResumeCreate(BaseModel):
    filename: str
    content: str

class ResumeResponse(BaseModel):
    id: int
    filename: str
    skills: str
    score: int
    user_id: int

    class Config:
        from_attributes = True

# ---------- JOB MATCH SCHEMAS ----------

class JobMatchRequest(BaseModel):
    jd_text: str

class JobMatchResponse(BaseModel):
    match_percentage: str
    matched_skills: List[str]
    missing_skills: List[str] # Add this line