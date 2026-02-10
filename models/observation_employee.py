from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid

class Employee(SQLModel, table=True):
    __tablename__ = "observation_employee" # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    public_id: str = Field(default_factory=lambda: str(uuid.uuid4()),
                    index=True,
                    unique=True)
    firstName: str
    lastName: str
    email: str
    password: str
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)