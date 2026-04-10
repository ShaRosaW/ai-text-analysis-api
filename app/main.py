import logging

from fastapi import FastAPI

from app.routes import router

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(router)