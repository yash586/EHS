from pydantic import BaseModel, Field, field_validator
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

class ObservationUpdate(BaseModel):
    title : str | None = None
    category_id: int | None = None
    employee_id: int | None = None
    location : str | None = None
    date: datetime | None = None