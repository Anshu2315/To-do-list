from typing import Optional
from fastapi import FastAPI
from todo.models.models import Todo, Todo_Pydantic, pydantic_model_creator
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello: World"}


class Status(BaseModel):
    message: str
