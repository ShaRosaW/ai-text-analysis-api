# AI Text Analysis API

A small FastAPI project for analyzing text using mock or AI-powered endpoints.

This project was built as a learning project to explore and gain hands-on experience with Python, FastAPI, and AI-driven APIs:
- Python project setup with virtual environments
- FastAPI for building APIs
- Pydantic for request and response models
- basic text analysis workflows such as summarization, keyword extraction, and action item extraction
- environment-based configuration using `.env`

## Purpose

The goal of this project is to experiment with building a simple backend API that processes and analyzes text using both mock logic and AI-based approaches.

## Features

- `GET /` health check endpoint
- `POST /summarize` returns a short summary
- `POST /keywords` extracts keywords
- `POST /action-items` extracts action items
- `POST /analyze` returns a combined analysis response

At the moment, the project supports mock responses when no API key is provided.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- OpenAI Python SDK

## Project Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd ai-text-analysis-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv  
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Create a `.env` file

add variable:

```bash
OPENAI_API_KEY=
```

If no API key is provided, the application will return mock responses.

## Run the project

```bash
uvicorn main:app --reload
```

Open in your browser:

- API root: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

## Example Request

### POST `/summarize`

```json
{  
  "text": "This is an example text that should be summarized."  
}
```

## Notes

This project is intentionally kept small and iterative. Future improvements may include:

- splitting the project into modules
- moving AI logic into a separate service layer
- adding tests
- adding support for real OpenAI responses through environment configuration