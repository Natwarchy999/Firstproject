from database.db import Base, engine
from fastapi import FastAPI
from routes.auth import router as auth_router

Base.metadata.create_all(engine)

app = FastAPI(title="this is for creating table")

app.include_router(auth_router)




