from fastapi import APIRouter, HTTPException
from models import ResumeJobInput
from services import resume_job_match

router = APIRouter()

@router.post("/analyse")
def analyse(data: ResumeJobInput):
    result = {}
    try:
        result["score"] = float(resume_job_match(data.resume, data.job))
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
