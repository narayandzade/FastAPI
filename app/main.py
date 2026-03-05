from fastapi import FastAPI
from app.database import Base, engine
from app.routers import main

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(main.router)