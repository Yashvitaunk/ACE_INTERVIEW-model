from fastapi import FastAPI

from models.llama_handler import generate_response

from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.jd_parser import read_jd
from utils.self_description_parser import read_self_description

from services.ats_service import (
    calculate_ats_score,
    generate_ai_ats_analysis
)

from services.roadmap_service import generate_roadmap
from services.question_service import generate_questions

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "ACE Interview AI Engine Running"
    }


@app.get("/test-llama")
def test_llama():

    answer = generate_response(
        "Explain Java in 3 lines."
    )

    return {
        "response": answer
    }


@app.get("/test-resume")
def test_resume():

    text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    return {
        "resume_text": text
    }


@app.get("/test-skills")
def test_skills():

    text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    skills = extract_skills(text)

    return {
        "skills": skills
    }


@app.get("/test-jd")
def test_jd():

    jd_text = read_jd(
        "sample_data/jd.txt"
    )

    return {
        "job_description": jd_text
    }


@app.get("/test-ats")
def test_ats():

    resume_text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    resume_skills = extract_skills(
        resume_text
    )

    jd_text = read_jd(
        "sample_data/jd.txt"
    )

    jd_skills = extract_skills(
        jd_text
    )

    result = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    return result


@app.get("/test-ai-ats")
def test_ai_ats():

    resume_text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    jd_text = read_jd(
        "sample_data/jd.txt"
    )

    self_description = read_self_description(
        "sample_data/self_description.txt"
    )

    analysis = generate_ai_ats_analysis(
        resume_text,
        jd_text,
        self_description
    )

    return {
        "analysis": analysis
    }


@app.get("/test-roadmap")
def test_roadmap():

    resume_text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    jd_text = read_jd(
        "sample_data/jd.txt"
    )

    self_description = read_self_description(
        "sample_data/self_description.txt"
    )

    roadmap = generate_roadmap(
        resume_text,
        jd_text,
        self_description
    )

    return {
        "roadmap": roadmap
    }


@app.get("/test-questions")
def test_questions():

    resume_text = extract_resume_text(
        "sample_data/resume.pdf"
    )

    jd_text = read_jd(
        "sample_data/jd.txt"
    )

    self_description = read_self_description(
        "sample_data/self_description.txt"
    )

    questions = generate_questions(
        resume_text,
        jd_text,
        self_description
    )

    return {
        "questions": questions
    }