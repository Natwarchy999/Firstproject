from fastapi import FastAPI
from app.core.db import Base, engine
from app.routes.auth import router as auth_router
from app.dependencies.limiter import limiter
from app.middleware.cors import cors_setup


app = FastAPI(title="FastAPI Backend")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "API is running",
    }

#1 cors setup
cors_setup(app)

#2 for rate limiting 
app.state.limiter = limiter

#3 for routing 
app.include_router(auth_router)








