from pydantic import BaseModel, Field
from typing import List, Optional

class Prediction(BaseModel):
    class_name: str = Field(..., alias="class")
    confidence: float

    class Config:
        populate_by_name = True


class AnalysisResponse(BaseModel):
    predictions: List[Prediction]
    ocr_text: Optional[str] = None
    explanation: str
    risk_level: str
    disclaimer: str
    heatmap: Optional[str] = None
