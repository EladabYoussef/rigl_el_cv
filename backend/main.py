from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import (
    analyse,
    parser,
    prepare,
    report
)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(analyse.router)
app.include_router(parser.router)
app.include_router(report.router)
app.include_router(prepare.router)
