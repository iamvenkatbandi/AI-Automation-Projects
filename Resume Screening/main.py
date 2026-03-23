import os
from parser import extract_text_from_pdf, extract_text_from_docx
from utils import extract_resume_data
from scorer import score_candidate
from export import export_to_csv

JOB_DESCRIPTION = """
Looking for a Python Developer with AI/ML skills, APIs, and data handling experience.
"""

def process_resumes():
    results = []
    folder = "resumes"

    if not os.path.exists(folder):
        print("❌ 'resumes' folder not found.")
        return results

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        print(f"\n📄 Processing: {file}")

        try:
            # Extract text
            if file.endswith(".pdf"):
                text = extract_text_from_pdf(path)
            elif file.endswith(".docx"):
                text = extract_text_from_docx(path)
            else:
                continue

            if not text.strip():
                print("⚠️ Empty file")
                continue

            # Extract data
            data = extract_resume_data(text)

            # Score
            score = score_candidate(data, JOB_DESCRIPTION)

            results.append({
                "file": file,
                "name": data["name"],
                "skills": ", ".join(data["skills"]),
                "experience": data["years_of_experience"],
                "education": data["education"],
                "score": score["score"],
                "reason": score["reason"]
            })

        except Exception as e:
            print(f"❌ Error: {e}")

    return results


def rank_candidates(results):
    return sorted(results, key=lambda x: x["score"], reverse=True)


def get_top_candidates(results, n=5):
    return results[:n]


def print_results(results):
    print("\n📊 FINAL RANKED CANDIDATES:\n")

    for i, r in enumerate(results, 1):
        print(f"{i}. {r['name']}")
        print(f"   Skills: {r['skills']}")
        print(f"   Experience: {r['experience']} years")
        print(f"   Score: {r['score']}/100")
        print(f"   Reason: {r['reason']}")
        print("-" * 40)


if __name__ == "__main__":
    print("🚀 Starting Resume Screening...")

    data = process_resumes()

    if not data:
        print("❌ No resumes processed")
        exit()

    ranked = rank_candidates(data)

    print_results(ranked)

    # Top 5
    top = get_top_candidates(ranked)
    print("\n🏆 TOP 5 CANDIDATES:\n")
    for c in top:
        print(f"{c['name']} - {c['score']}")

    # Export
    export_to_csv(ranked)
