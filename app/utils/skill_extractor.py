import re
from app.utils.skills import SKILLS_DB

def extract_skills(text: str):
    if not text:
        return []
    
    text = text.lower()
    found_skills = []
    
    for skill in SKILLS_DB:
        # \b ensures we match the WHOLE word only. 
        # This stops "php" from being found in "photography"
        pattern = rf"\b{re.escape(skill.lower())}\b"
        if re.search(pattern, text):
            found_skills.append(skill)
            
    return list(set(found_skills))