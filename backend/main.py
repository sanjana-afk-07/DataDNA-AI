from fastapi import FastAPI, UploadFile, File
import shutil
import os

from dna_engine.generator import generate_datadna


app = FastAPI(
    title="DataDNA AI",
    description="AI-powered dataset fingerprinting platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "DataDNA AI",
        "message": "Every dataset has a fingerprint."
    }


@app.post("/analyze")
async def analyze_dataset(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    dna = generate_datadna(file_path)

    return dna
