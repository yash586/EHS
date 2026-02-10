from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum
import uuid

class Observation(SQLModel, table=True):
    __tablename__ = "observation_records" # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    public_id: str = Field(default_factory=lambda:str(uuid.uuid4()),
                    index=True,
                    unique=True)
    title:str
    category_id:int
    employee_id:int
    location: str | None
    date: datetime = Field(default_factory=datetime.now)
    active: bool = Field(default=True)
    createdAt: datetime = Field(default_factory=datetime.now)