from models.llama_handler import generate_response


def generate_questions(resume_text, jd_text, self_description=""):

    resume_text = resume_text[:500]
    jd_text = jd_text[:300]
    self_description = self_description[:300]

    prompt = f"""
Resume:
{resume_text}

Job Description:
{jd_text}

Self Description:
{self_description}

Generate exactly 3 TECHNICAL QUESTIONS.

For each provide:

Question:
Intention: One short line only.
Model Answer: One short line only.

Then generate exactly 3 BEHAVIORAL QUESTIONS.

For each provide:

Question:
Intention: One short line only.
Model Answer: One short line only.

Keep the entire response under 250 words.
Do not write long explanations.
"""

    return generate_response(prompt)