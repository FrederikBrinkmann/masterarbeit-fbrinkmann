LLM Pipeline Thesis - Repo

Projektstruktur (kurz):

- `backend/`: FastAPI Backend
- `worker/`: Asynchroner Worker
- `dummy_ticket_api/`: Kleines Zielsystem (Flask)
- `data/`: Beispieldaten
- `evaluation/`: Metriken und Experimente

Lokales Starten (kurz):

1. Backend:

python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000

2. Dummy Ticket API:

pip install flask
python dummy_ticket_api/app.py

3. Worker:

python worker/worker.py
