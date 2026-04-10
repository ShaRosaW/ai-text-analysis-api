# AI Text Analysis API

A lightweight FastAPI application for analyzing text using both mock logic and AI-powered endpoints.

This project was built as a learning project to explore and gain hands-on experience with Python, FastAPI, and AI-driven APIs with a focus on:

- Python project setup with virtual environments
- FastAPI for building API-based applications
- Pydantic for request and response models
- Text analysis workflows such as summarization, keyword extraction, and action item extraction
- Environment-based configuration using `.env`
- Structuring backend code into modular components such as routes, services, models, and configuration

## Purpose

The goal of this project is to experiment with building a simple backend API that processes and analyzes text using both mock logic and AI-based approaches.

## Features

- `GET /` health check endpoint
- `POST /summarize` returns a short summary
- `POST /keywords` extracts keywords
- `POST /action-items` extracts action items
- `POST /analyze` returns a combined analysis response


## How it works

The API exposes multiple endpoints that process input text and return structured outputs such as summaries, keywords, and action items.

When no API key is provided, the application returns mock responses. This makes it possible to run and test the project locally without external API access. When a valid OpenAI API key is configured, the endpoints can be extended to use real AI-generated results.

The project is structured into separate modules for:

- `routes` for API endpoints
- `services` for business logic
- `models` for request and response schemas
- `core` for configuration handling

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- OpenAI Python SDK

## Project Structure  
  
```text  
ai-text-analysis-api/  
├── app/  
│ ├── main.py  
│ ├── models.py  
│ ├── routes.py  
│ ├── core/  
│ │ └── config.py  
│ └── services/  
│ └── ai_service.py  
├── .gitignore  
├── README.md  
├── requirements.txt


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
uvicorn app.main:app --reload
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

This project is intentionally kept small and iterative, focusing on strengthening my backend and AI-driven development while also expanding into fullstack development, serving as a practical opportunity to re-engage with frontend development using React and TypeScript.

Potential next improvements include:

- Developing a simple frontend interface using React and TypeScript
- Creating reusable UI components for text input and analysis results
- Integrating frontend and backend via REST API communication

- Adding support for real AI responses through environment-based configuration
- Improving response parsing and output structure
- Adding unit and integration tests
- Extending the analysis workflow with additional endpoints or multi-step processing

This project will continue to evolve as I further develop my skills in Python, backend development, frontend technologies, and AI-driven applications.