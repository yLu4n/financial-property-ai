from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.api.schemas import AnalysisRequest
from src.services.analysis_service import run_full_analysis

app = FastAPI(
    title="Financial Property Analysis API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analysis")
def analyze(request: AnalysisRequest):

    result = run_full_analysis(
        financial_data=request.financial_data.model_dump(),
        property_value=request.property_value,
        monthly_rent=request.monthly_rent
    )

    return {
        "success": True,
        "data": result
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}