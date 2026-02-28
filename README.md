# 🚀 SmartHire AI – Resume Classification System

SmartHire AI is a full-stack Machine Learning web application that analyzes resumes and predicts the most suitable technical department:

- DevOps  
- Backend Engineering  
- Frontend Engineering  
- Artificial Intelligence  

It uses Natural Language Processing (TF-IDF), Logistic Regression, and Explainable AI techniques to provide both prediction confidence and feature-level explanation.

---

## 🔥 Live Demo

🌐 Live App: https://smarthire-ai-ml5m.onrender.com  

---

## 🧠 Features

✅ Resume PDF Upload  
✅ Text Extraction from PDF  
✅ Department Prediction  
✅ Confidence Scores (%)  
✅ Explainable AI (Top Influencing Keywords)  
✅ REST API Endpoint  
✅ SQLite Database Logging  
✅ Dockerized Deployment  
✅ Production-ready FastAPI backend  

---

## 🏗 Architecture
Resume PDF → Text Extraction (PyPDF2)
↓
TF-IDF Vectorization (1–3 ngrams)
↓
ColumnTransformer (Text + Experience)
↓
Logistic Regression Classifier
↓
Confidence Scores + Top Feature Explanation
↓
FastAPI Web Interface

---

## 📊 Machine Learning Pipeline

- TF-IDF (1–3 grams)
- Stopword removal
- Feature scaling for numeric input
- Logistic Regression (predict_proba enabled)
- Balanced synthetic dataset (1000+ samples)

Explainability:
- Extracts top weighted contributing features for prediction.

---

## 📁 Project Structure

smarthire-ai/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│
├── data/
│ └── training_dataset.csv
│
├── templates/
│ └── index.html
│
├── train_model.py
├── generate_dataset.py
├── requirements.txt
├── Dockerfile
├── model.pkl
└── README.md

---

## 🐳 Run Using Docker

### Build Image

```bash
docker build -t smarthire-ai .
docker run -p 8000:8000 smarthire-ai
http://localhost:8000

🛠 Run Locally (Without Docker)
pip install -r requirements.txt
python train_model.py
uvicorn app.main:app --reload

📡 API Usage
POST /predict

Example:
POST /predict?skills=Python AWS Docker&years_experience=3

{
  "predicted_department": "DevOps",
  "confidence_scores": [
    ["DevOps", 58.14],
    ["Backend", 24.79],
    ["Frontend", 10.28],
    ["AI", 6.79]
  ]
}

🔎 Explainability Example

Predicted: DevOps
Confidence: 58.14%

Top Influencing Words:

infrastructure

automated

cloud

deployments

managed

💡 Future Improvements

SHAP-based explainability

Real-world resume dataset integration

Role-based scoring system

Job matching system

Advanced UI dashboard

Cloud logging with PostgreSQL

👨‍💻 Author

Mohammad Akbar
B.Tech Computer Science
Python | AWS | Machine Learning | Backend Development

📜 License

This project is open-source and available for learning and educational use.