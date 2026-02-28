# 🚀 SmartHire AI – Resume Classification & Explainable ML System

SmartHire AI is a full-stack Machine Learning web application that analyzes resumes and predicts the most suitable technical department:

- 🔧 DevOps  
- 🖥 Backend Engineering  
- 🎨 Frontend Engineering  
- 🤖 Artificial Intelligence  

The system combines Natural Language Processing (TF-IDF), structured feature engineering, Logistic Regression, and Explainable AI to provide both prediction confidence and interpretable insights.

---

## 🔍 What Makes This Project Different?

Unlike simple keyword classifiers, SmartHire AI:

- Uses TF-IDF with bi/tri-grams  
- Combines text + years of experience  
- Provides probability-based confidence scores  
- Shows top contributing keywords for explainability  
- Supports Resume PDF ingestion  
- Is fully Dockerized for production deployment  

---

## 🧠 Core Features

✅ Resume PDF Upload  
✅ Automatic Text Extraction  
✅ Department Prediction  
✅ Confidence Scores (%)  
✅ Explainable AI (Top Influencing Words)  
✅ REST API Endpoint  
✅ SQLite Database Logging  
✅ Dockerized Deployment  
✅ Production-ready FastAPI Backend  

---

## 🏗 System Architecture


Resume PDF
↓
Text Extraction (PyPDF2)
↓
TF-IDF Vectorization (1–3 ngrams)
↓
ColumnTransformer
(Text Features + Experience Scaling)
↓
Logistic Regression Classifier
↓
Confidence Scores + Feature Explanation
↓
FastAPI Web Application


---

## 📊 Machine Learning Pipeline

- TF-IDF (n-gram range: 1–3)
- Stopword removal
- Feature scaling for numeric data
- Logistic Regression (predict_proba enabled)
- Synthetic balanced dataset (1000+ samples)
- Feature-weight based explainability

---

## 📁 Project Structure


smarthire-ai/
│
├── app/
│ ├── main.py
│ ├── models.py
│ └── database.py
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

## 🐳 Run Using Docker (Recommended)

### 1️⃣ Build Image

```bash
docker build -t smarthire-ai .
2️⃣ Run Container
docker run -p 8000:8000 smarthire-ai
3️⃣ Open in Browser
http://localhost:8000
🛠 Run Locally (Without Docker)
pip install -r requirements.txt
python generate_dataset.py
python train_model.py
uvicorn app.main:app --reload
📡 API Endpoint
POST /predict

Example:

POST /predict?skills=Python AWS Docker&years_experience=3

Example Response:

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

Predicted Department: DevOps
Confidence: 58.14%

Top Influencing Words:

infrastructure

automated

cloud

deployments

managed

This makes the model decision transparent and interpretable.

📈 Future Improvements

SHAP-based local explainability

Real-world resume dataset integration

Role-to-job matching system

PostgreSQL production database

Modern dashboard UI

Cloud-native CI/CD integration

👨‍💻 Author

Mohammad Akbar
B.Tech – Computer Science

Skills: Python | AWS | Machine Learning | FastAPI | Docker | Backend Systems

📜 License

This project is open-source and intended for educational and research purposes.


---

# 🔥 Why This Version Is Better

- Clean formatting
- Strong technical language
- Proper spacing
- Professional structure
- Clear architecture explanation
- Docker-first deployment
- No Render dependency
- Looks like production software documentation

---

# 🚀 Next Upgrade (Optional but Powerful)

We can add:

- GitHub badges (Python, Docker, FastAPI)
- Screenshots section
- Architecture diagram image
- Tech stack badge section
- “Why I Built This” section (very impressive for internships)

If you want to make this **top 5% level GitHub**, say:

> Make it elite.

And we’ll take it up another level.
