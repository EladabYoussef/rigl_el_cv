from pydantic import BaseModel

class ResumeJobInput(BaseModel):
    resume: str
    job: str
