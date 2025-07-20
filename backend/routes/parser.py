from fastapi import APIRouter, HTTPException, UploadFile, File
from services import text_from_pdf, extract_entities
import spacy

nlp = spacy.load("./training/nlp_model")
router = APIRouter()

@router.post("/parse")
async def parse(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        text = text_from_pdf(file_bytes)
        entities = extract_entities(text, nlp)

        return entities
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))