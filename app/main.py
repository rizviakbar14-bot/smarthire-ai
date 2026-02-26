from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import os
import pandas as pd

app = FastAPI(title="SmartHire AI")

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
    return {"predicted_department": prediction}