from fastapi import FastAPI, Query
from sqlmodel import select
from typing import Annotated
from dependencies import SessionDep
from models import User, UserPublic

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/users/", response_model=list[UserPublic])
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users