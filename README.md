# AI Text Analysis API

A fullstack application for analyzing text using a FastAPI backend and a React + TypeScript frontend.

The application allows users to submit text and receive structured analysis results, including summaries, keywords, and action items.

This project was built as a hands-on learning project to explore backend development with Python and FastAPI, while also re-engaging with frontend development using React and TypeScript.

---

## Purpose

The goal of this project is to experiment with building a fullstack application that processes and analyzes text using both mock logic and AI-based approaches.

It focuses on:
- designing and structuring a backend API
- building a simple frontend interface
- integrating frontend and backend through REST APIs
- exploring how AI-driven features can be applied in real-world workflows

---

## Features

### Backend (FastAPI)

- `GET /` health check endpoint
- `POST /summarize` returns a short summary
- `POST /keywords` extracts keywords
- `POST /action-items` extracts action items
- `POST /analyze` returns a combined analysis response

Supports:
- mock responses (default, no API key required)
- optional real AI integration via environment configuration

---

### Frontend (React + TypeScript)

- Text input form for submitting content
- Displays:
  - summary
  - keywords
  - action items
- Loading and error states
- Reusable UI components:
  - `TextForm`
  - `ResultCard`
- API integration with configurable base URL via environment variables

---

### Environment Configuration

The project uses environment variables for configuration:

- Backend: `.env`
- Frontend: `frontend/.env`

Example files are provided:
- `.env.example`
- `frontend/.env.example`

---

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- OpenAI Python SDK (optional)

### Frontend
- React
- TypeScript
- Vite

---

## Project Structure  
  
```text  
ai-text-analysis-api/  
│
├── app/  
│   ├── core/               # config and environment setup
│   │   └── config.py  
│   ├── services/           # business logic and AI handling
│   │   └── ai_service.py  
│   ├── main.py             # FastAPI entrypoint
│   ├── models.py           # request/response models
│   ├── routes.py           # API endpoints
│  
├── frontend/  
│   ├── src/  
│   │   ├── components/     # reusable UI components  
│   │   ├── App.tsx         # main application component
│   │   ├── index.css       # global styles 
│   │   └── main.tsx        # React entrypoint
│   └── .env.example        # example frontend environment config  
│  
├── .env.example            # example backend environment config
├── .gitignore  
├── README.md  
└── requirements.txt
```

---

## How It Works

The project consists of a FastAPI backend and a React + TypeScript frontend.

### Backend
- Handles text analysis logic
- Exposes REST endpoints
- Uses modular architecture (routes, services, models)

### Frontend
- Sends user input to the backend API
- Communicates with the backend via REST API calls
- Displays structured results
- Uses reusable components to separate logic and presentation

### AI / Mock behavior
- If no `OPENAI_API_KEY` is set → mock responses are returned. 
  This allows the project to run locally without external API access while still demonstrating the full application flow.
- If configured → real AI responses can be enabled

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/ShaRosaW/ai-text-analysis-api.git
cd ai-text-analysis-api
```

### 2. Backend setup

#### 2.1 Create and activate a virtual environment

```bash
python3 -m venv venv  
source venv/bin/activate
```

#### 2.2 Install dependencies

```bash
pip3 install -r requirements.txt
```

#### 2.3 Create `.env` file 

In the root of the project:

Copy the example file:
```bash
cp .env.example .env
```

Add your API key:
```env
OPENAI_API_KEY=your_api_key_here
```

> If no API key is provided, the application will return mock responses.

---

### 3. Frontend setup

#### 3.1 Install dependencies within frontend folder

```bash
cd frontend  
npm install
```

#### 3.2 Create `.env` file

Inside the `frontend/` folder:

Copy the example file:
```bash
cp .env.example .env
```

Set the API base URL:
```env
VITE_API_URL=http://127.0.0.1:8000
```

---

## Run the project

### Start backend

```bash
uvicorn app.main:app --reload
```

### Start frontend

```bash
cd frontend  
npm run dev
```

---

## Access the application

- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Example API Request

### POST `/analyze`

```json
{  
  "text": "This is an example text that should be analyzed."
}
```

---

## Notes

- This project serves as a learning project for Python, FastAPI, and React.
- The focus was on understanding architecture, API design, and integration between frontend and backend.

---

## Future Improvements

This project is intentionally kept small and iterative, focusing on strengthening my backend and AI-driven development while gradually expanding into fullstack development through React and TypeScript.

Potential next improvements include:

- Improving frontend UI/UX (layout, interaction, loading states)
- Creating more reusable UI components
- Enhancing frontend state management
- Enabling real AI responses through environment-based configuration
- Improving response parsing and output structure
- Adding unit and integration tests
- Extending the analysis workflow with additional endpoints or multi-step processing

---

## Author
Sharon

---