# backend/app/models/__init__.py
# Pydantic models and schema definitions placeholder
from pydantic import BaseModel

class IngestRequest(BaseModel):
    source: str
    payload: dict

class JobStatus(BaseModel):
    job_id: str
    status: str
    result: dict | None = None
