from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(Text)
    skills = Column(String)
    score = Column(Integer)
    # Changed: Removed the strict link to a user for now
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)