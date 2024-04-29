from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:Kevin254!@postgres/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Role(str, Enum):
    admin = "admin"
    user = 'user'
    student = "student"


class Gender(str, Enum):
    male = "male"
    female = 'female'


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name:Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[str]]
