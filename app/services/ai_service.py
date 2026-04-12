import logging

from fastapi import HTTPException
from openai import OpenAI

from app.core.config import get_openai_api_key

logger = logging.getLogger(__name__)


def validate_text(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")


def get_openai_client():
    api_key = get_openai_api_key()
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def summarize_text(text: str):
    validate_text(text)
    logger.info(f"Summarize request received. Length: {len(text)}")

    client = get_openai_client()

    if not client:
        return {"summary": f"(Mock) Summary: {text[:50]}..."}

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Summarize the given text concisely in English."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return {"summary": response.output_text}


def extract_keywords(text: str):
    validate_text(text)
    logger.info("Keyword extraction request received")

    client = get_openai_client()

    if not client:
        return {"keywords": ["example", "mock", "keyword1", "keyword2"]}

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Extract 5 relevant keywords from the text. Return them as a comma-separated list."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    keywords = [kw.strip() for kw in response.output_text.split(",")]
    return {"keywords": keywords}


def extract_action_items(text: str):
    validate_text(text)
    logger.info("Action items extraction request received")

    client = get_openai_client()

    if not client:
        return {"action_items": ["mock action 1", "mock action 2"]}

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Extract 3 clear action items from the text. Return them as a comma-separated list."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    action_items = [item.strip() for item in response.output_text.split(",")]
    return {"action_items": action_items}


def analyze_text(text: str):
    validate_text(text)
    logger.info("Full analysis request received")

    return {
        "summary": f"This is a (mock) summary of the provided text: {text[:120]}...",
        "keywords": ["analysis", "text", "example", "mock", "demo"],
        "action_items": [
            "Review the provided text",
            "Identify key insights",
            "Take follow-up actions based on the analysis"
        ]
    }