def calculate_score(skills: list, experience_years: int = 0):
    score = len(skills) * 5
    if experience_years >= 3:
        score += 20
    elif experience_years >= 1:
        score += 10
    return min(score, 100)