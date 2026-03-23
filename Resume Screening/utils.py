import re

def extract_name(text):
    lines = text.split("\n")
    for line in lines[:5]:
        if line.strip():
            return line.strip()
    return "Unknown"


def extract_skills(text):
    skills_list = [
        "python", "java", "c++", "machine learning", "deep learning",
        "sql", "pandas", "numpy", "tensorflow", "pytorch",
        "html", "css", "javascript", "react", "node", "apis"
    ]

    found_skills = []
    text_lower = text.lower()

    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill.capitalize())

    return list(set(found_skills))


def extract_experience(text):
    match = re.search(r"(\d+)\s+years", text.lower())
    if match:
        return match.group(1)
    return "0"


def extract_education(text):
    degrees = ["b.tech", "bachelor", "m.tech", "master", "bsc", "msc"]
    text_lower = text.lower()

    for degree in degrees:
        if degree in text_lower:
            return degree.upper()

    return "Unknown"


def extract_resume_data(resume_text):
    return {
        "name": extract_name(resume_text),
        "skills": extract_skills(resume_text),
        "years_of_experience": extract_experience(resume_text),
        "education": extract_education(resume_text)
    }
