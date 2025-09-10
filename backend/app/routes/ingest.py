# backend/app/routes/ingest.py
from fastapi import APIRouter, HTTPException
from ..models import IngestRequest, JobStatus

router = APIRouter(prefix="/ingest")

@router.post("/")
async def ingest(req: IngestRequest):
    # placeholder: in Realität würde ein Job enqueued werden
    return {"job_id": "job-123", "status": "queued"}
