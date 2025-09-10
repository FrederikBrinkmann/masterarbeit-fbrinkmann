# backend/app/main.py
# Einstiegspunkt für die API (FastAPI)
from fastapi import FastAPI

app = FastAPI(title="LLM Pipeline Thesis - Backend")

@app.get("/status")
async def status():
    return {"status": "ok"}

# Weitere Routen werden in `backend/app/routes` definiert und importiert hier bei Bedarf.
