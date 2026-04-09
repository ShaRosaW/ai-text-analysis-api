# AI Text Analysis API

A lightweight FastAPI application for analyzing text using both mock logic and AI-powered endpoints.

This project was built as a learning project to explore and gain hands-on experience with Python, FastAPI, and AI-driven APIs:
- Python project setup with virtual environments
- FastAPI for building APIs
- Pydantic for request and response models
- Basic text analysis workflows such as summarization, keyword extraction, and action item extraction
- Environment-based configuration using `.env`

## Purpose

The goal of this project is to experiment with building a simple backend API that processes and analyzes text using both mock logic and AI-based approaches.

## Features

- `GET /` health check endpoint
- `POST /summarize` returns a short summary
- `POST /keywords` extracts keywords
- `POST /action-items` extracts action items
- `POST /analyze` returns a combined analysis response

At the moment, the project supports mock responses when no API key is provided.

## How it works

The API exposes several endpoints that process input text and return structured outputs such as summaries, keywords, and action items.

When no API key is provided, the application falls back to mock responses. When a valid OpenAI API key is configured, the endpoints can be extended to use real AI-generated results.

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
git clone https://github.com/ShaRosaW/ai-text-analysis-api.git
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

Create a `.env` file in the root of the project and add:

```env
OPENAI_API_KEY=your_api_key_here
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

## Future Improvements

This project is intentionally kept small and iterative, with a focus on learning and exploring backend and AI-driven development. It also serves as a foundation for further improvements in architecture and AI integration.

Potential next improvements include:

- Refactoring the project into modular components (routes, services, models)
- Moving AI-related logic into a dedicated service layer
- Adding unit and integration tests
- Supporting real AI responses through environment-based configuration

This project will continue to evolve as I further develop my skills in Python, backend development, and AI applications.