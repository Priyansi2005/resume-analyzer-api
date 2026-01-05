def match_resume_jd(resume_skills: list, jd_text: str):
    jd_text = jd_text.lower()
    matched = [skill for skill in resume_skills if skill.lower() in jd_text]
    if not resume_skills: return 0, []
    return int((len(matched) / len(resume_skills)) * 100), matched