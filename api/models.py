from sqlmodel import SQLModel, Field
from datetime import datetime

class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
    created_at: datetime | None

class UserCreate(UserBase):
    password: str
    created_at: datetime | None = Field(default=datetime.now())

class UserUpdate(UserBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None

class UserPublic(UserBase):
    create_at: datetime