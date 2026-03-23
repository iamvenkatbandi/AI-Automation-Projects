def score_candidate(resume_data, job_description):
    score = 0
    reason = []

    required_skills = ["Python", "Machine Learning", "SQL", "Apis"]

    candidate_skills = resume_data.get("skills", [])

    matched = [s for s in required_skills if s in candidate_skills]

    # Skill score
    skill_score = len(matched) * 15
    score += skill_score

    if matched:
        reason.append(f"Skills matched: {', '.join(matched)}")

    # Experience score
    try:
        exp = int(resume_data.get("years_of_experience", 0))
        exp_score = min(exp * 5, 20)
        score += exp_score
        reason.append(f"{exp} years experience")
    except:
        pass

    # Education bonus
    if "B.TECH" in resume_data.get("education", ""):
        score += 10
        reason.append("Relevant degree")

    return {
        "score": min(score, 100),
        "reason": ", ".join(reason) if reason else "Basic match"
    }
