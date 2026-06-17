from models.llama_handler import generate_response


def generate_roadmap(
    resume_text,
    jd_text,
    self_description=""
):

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

Create a Day 1 to Day 7 interview preparation roadmap.

Format:

Day 1:
Day 2:
Day 3:
Day 4:
Day 5:
Day 6:
Day 7:

Each day should contain only 2 short tasks.

Keep total response under 150 words.
"""

    return generate_response(prompt)