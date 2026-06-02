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
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class ProjectBase(SQLModel):
    name: str

class Project(ProjectBase, table=True):
    __tablename__ = "projects"
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="users.id")
    created_at: datetime | None = Field(default=datetime.now(UTC))

class ProjectCreate(ProjectBase):
    pass

class ProjectPublic(ProjectBase):
    created_at: datetime
    owner_id: int
    id: int

class TaskBase(SQLModel):
    title: str
    description: str
    assigned_to: int | None
    status: str | None
    due_date: datetime | None

class Task(TaskBase, table=True):
    __tablename__ = "tasks"
    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="projects.id")
    created_at: datetime | None = Field(default=datetime.now(UTC))

class TaskCreate(TaskBase):
    project_id: int
    due_date: datetime | None = None

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    assigned_to: int | None = None
    status: str | None = None
    due_date: datetime | None = None

class TaskPublic(TaskBase):
    id: int
    project_id: int
    created_at: datetime