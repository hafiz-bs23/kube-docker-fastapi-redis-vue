from typing import Union

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}