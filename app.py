from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


MODEL_DIR = Path(__file__).resolve().parent / "model"
vectorizer = joblib.load(MODEL_DIR / "embedding_model.pkl")
model = joblib.load(MODEL_DIR / "model.pkl")

app = FastAPI(
    title="Personality Detector API",
    description="Predicts whether text is associated with an introvert or extrovert personality.",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    text: str = Field(
        min_length=1,
        description="Text to analyze",
        examples=["I enjoy quiet time practicing yoga."],
    )


class PredictionResponse(BaseModel):
    personality: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict_personality(request: PredictionRequest) -> PredictionResponse:
    if not request.text.strip():
        raise HTTPException(status_code=422, detail="Text must not be blank.")

    features = vectorizer.transform([request.text])
    prediction = str(model.predict(features)[0])
    return PredictionResponse(personality=prediction)