from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, select
import models
from contextlib import asynccontextmanager
from db import create_db_and_tables, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root() -> str:
    return "Eliise"