from pydantic import BaseModel, Field, field_validator
from typing import Union
from enum import Enum
from datetime import datetime

class ObservationBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    category_id: int
    employee_id: int
    location: str|None
    date: datetime

    @field_validator("date", mode="before")
    def parse_date(cls,v):
        if isinstance(v, str):
            return datetime.strptime(v, "%d/%m/%Y")
        return v

class ObservationResponse(ObservationBase):
    public_id:str
    createdAt:datetime