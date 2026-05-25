from fastapi import FastAPI, Query, HTTPException
from sqlmodel import select
from typing import Annotated
from dependencies import SessionDep
from models import User, UserPublic, UserCreate, UserUpdate

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

@app.get("/users/{user_id}", response_model=UserPublic)
def read_users(
    session: SessionDep,
    user_id: int,
) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserPublic)
def create_user(session: SessionDep, user: UserCreate):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return 

@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

@app.patch("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserUpdate, session: SessionDep):
    user_db = session.get(User, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(user_data)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db