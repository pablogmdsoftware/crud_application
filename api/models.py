from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime, UTC

class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default=datetime.now(UTC))
    password: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None

class UserPublic(UserBase):
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None