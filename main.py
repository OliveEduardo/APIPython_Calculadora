import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

origins = ["http://localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
