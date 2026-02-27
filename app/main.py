from urllib import request

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import os
import pandas as pd
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Prediction
from sqlalchemy.orm import Session

app = FastAPI(title="SmartHire AI")
Prediction.metadata.create_all(bind=engine)

# Templates setup
templates = Jinja2Templates(directory="templates")

# Load trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")
model = pickle.load(open(model_path, "rb"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict-form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    skills: str = Form(...),
    years_experience: int = Form(...)
):

    input_data = pd.DataFrame(
        [[skills, years_experience]],
        columns=["skills", "years_experience"]
    )

    prediction = model.predict(input_data)[0]

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": prediction}
    )


@app.post("/predict")
def predict_api(skills: str, years_experience: int):
    input_data = pd.DataFrame(
        [[skills, years_experience]],
        columns=["skills", "years_experience"]
    )
    prediction = model.predict(input_data)[0]
    db: Session = SessionLocal()

    new_entry = Prediction(
        skills=skills,
        experience=str(years_experience),
        prediction=prediction
    )

    db.add(new_entry)
    db.commit()
    db.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": prediction}
    )
    return {"predicted_department": prediction}

@app.get("/admin", response_class=HTMLResponse)
def view_predictions():
    db: Session = SessionLocal()
    records = db.query(Prediction).all()
    db.close()

    html = "<h1>Saved Predictions</h1><ul>"
    for r in records:
        html += f"<li>{r.skills} | {r.experience} | {r.prediction} | {r.created_at}</li>"
    html += "</ul>"

    return html
