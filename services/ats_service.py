from models.llama_handler import generate_response


def calculate_ats_score(resume_skills, jd_skills):

    matched = []

    missing = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    score = int(
        (len(matched) / len(jd_skills)) * 100
    ) if jd_skills else 0

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing[:4]
    }


def generate_ai_ats_analysis(
    resume_text,
    jd_text,
    self_description
):

    resume_text = resume_text[:1000]
    jd_text = jd_text[:500]
    self_description = self_description[:500]

    prompt = f"""
Resume:
{resume_text}

Self Description:
{self_description}

Job Description:
{jd_text}

Analyze the candidate against the job description.

Provide:

ATS SCORE (0-100)

TOP STRENGTHS

TOP 4 SKILL GAPS

RESUME IMPROVEMENTS

Keep the response concise and practical.
"""

    return generate_response(prompt)