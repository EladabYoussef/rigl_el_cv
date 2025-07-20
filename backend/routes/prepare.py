from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.parser import text_from_pdf

router = APIRouter()

@router.post("/prepare")
async def prepare_input(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        file_bytes = await resume.read()
        resume_text = text_from_pdf(file_bytes)
        job_text = job_description

        return {
            "resume": resume_text,
            "job": job_text
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))