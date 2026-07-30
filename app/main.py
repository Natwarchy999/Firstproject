from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings


app = FastAPI(title="FastAPI Backend")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "API is running",
    }

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins =settings.ORIGINS,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers =["*"]
)




