import pandas as pd
import random

skills_pool = [
    "Python", "FastAPI", "SQL", "AWS", "Docker",
    "React", "NodeJS", "Tensorflow", "NLP",
    "HTML", "CSS", "Kubernetes", "Flask"
]

departments = {
    "Backend": ["Python", "FastAPI", "SQL", "Docker"],
    "Frontend": ["React", "HTML", "CSS"],
    "AI": ["Tensorflow", "NLP", "Python"],
    "DevOps": ["Docker", "Kubernetes", "AWS"]
}

data = []

for _ in range(500):
    dept = random.choice(list(departments.keys()))
    dept_skills = departments[dept]
    extra_skills = random.sample(skills_pool, 2)
    
    skills = list(set(dept_skills + extra_skills))
    years = random.randint(0, 6)
    
    data.append({
        "skills": " ".join(skills),
        "years_experience": years,
        "department": dept
    })

df = pd.DataFrame(data)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "training_dataset.csv")

df.to_csv(file_path, index=False)
print("Dataset Created Successfully")