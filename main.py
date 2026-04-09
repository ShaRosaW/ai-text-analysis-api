import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# --- Models ---
class TextInput(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    summary: str
    keywords: list[str]
    action_items: list[str]


# --- Helpers ---
def validate_text(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


# --- Routes ---
@app.get("/")
def read_root():
    return {"message": "API is running"}


@app.post("/summarize")
def summarize(input: TextInput):
    validate_text(input.text)
    logger.info(f"Summarize request received. Length: {len(input.text)}")

    client = get_openai_client()

    if not client:
        return {
            "summary": f"(Mock) Summary: {input.text[:50]}..."
        }

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "Summarize the given text concisely in English."
                },
                {
                    "role": "user",
                    "content": input.text
                }
            ]
        )

        return {
            "summary": response.output_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while summarizing text: {str(e)}")


@app.post("/keywords")
def extract_keywords(input: TextInput):
    validate_text(input.text)
    logger.info("Keyword extraction request received")

    client = get_openai_client()

    if not client:
        return {
            "keywords": ["example", "mock", "keyword1", "keyword2"]
        }

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "Extract 5 relevant keywords from the text. Return them as a comma-separated list."
                },
                {
                    "role": "user",
                    "content": input.text
                }
            ]
        )

        keywords = [kw.strip() for kw in response.output_text.split(",")]
        return {
            "keywords": keywords
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while extracting keywords: {str(e)}")


@app.post("/action-items")
def extract_action_items(input: TextInput):
    validate_text(input.text)
    logger.info("Action items extraction request received")

    client = get_openai_client()

    if not client:
        return {
            "action_items": ["mock action 1", "mock action 2"]
        }

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": "Extract 3 clear action items from the text. Return them as a comma-separated list."
                },
                {
                    "role": "user",
                    "content": input.text
                }
            ]
        )

        action_items = [item.strip() for item in response.output_text.split(",")]
        return {
            "action_items": action_items
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while extracting action items: {str(e)}")


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_text(input: TextInput):
    validate_text(input.text)
    logger.info("Full analysis request received")

    return {
        "summary": f"(Mock) Summary: {input.text[:50]}...",
        "keywords": ["example", "mock", "keyword"],
        "action_items": ["mock action"]
    }