from fastapi import APIRouter, HTTPException

from app.models import TextInput, AnalysisResponse
from app.services.ai_service import (
    summarize_text,
    extract_keywords,
    extract_action_items,
    analyze_text,
)

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "API is running"}


@router.post("/summarize")
def summarize(input: TextInput):
    try:
        return summarize_text(input.text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/keywords")
def keywords(input: TextInput):
    try:
        return extract_keywords(input.text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/action-items")
def action_items(input: TextInput):
    try:
        return extract_action_items(input.text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze", response_model=AnalysisResponse)
def analyze(input: TextInput):
    try:
        return analyze_text(input.text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))