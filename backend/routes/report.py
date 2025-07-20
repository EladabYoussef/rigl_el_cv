from fastapi import APIRouter, HTTPException

from models import ResumeJobInput
from services import make_report

router = APIRouter()

@router.post("/report")
def report(data: ResumeJobInput):
    try:
        result = make_report(data.resume, data.job)
        return {"report": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
