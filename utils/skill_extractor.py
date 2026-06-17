SKILLS_DB = [
    "java",
    "python",
    "javascript",
    "react",
    "node.js",
    "express.js",
    "mongodb",
    "mysql",
    "html",
    "css",
    "git",
    "github",
    "jwt",
    "rest api",
    "docker",
    "aws",
    "c++",
    "oop",
    "dbms",
    "computer networks",
    "data structures",
    "algorithms",
    "numpy",
    "pandas",
    "scikit-learn",
    "opencv"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))