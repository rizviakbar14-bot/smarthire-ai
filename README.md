# SmartHire AI

AI-powered job role classifier built with FastAPI and Docker.

## Tech Stack
- FastAPI
- Scikit-learn
- Jinja2
- Docker

## Run Locally
uvicorn app.main:app --reload

## Run With Docker
docker build -t smarthire-ai .
docker run -p 8000:8000 smarthire-ai
