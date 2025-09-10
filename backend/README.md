Backend
=======

Minimaler FastAPI-Backend-Startpunkt für die LLM-Pipeline-Thesis.

Starten (lokal, mit Virtualenv):

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
