from pydantic import BaseModel, Field, field_validator, EmailStr, ValidationInfo
from datetime import datetime
import re

class EmployeeBase(BaseModel):
    firstName: str = Field(min_length=1)
    lastName: str = Field(min_length=1)
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("password")
    def validate_password(cls,v:str, info:ValidationInfo):
        if(len(v) < 8):
            raise ValueError("password must be 8 characters long")
        if not re.search(r"[a-z]",v):
            raise ValueError("Password must contain a lowercase letter")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain a upper case letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain a number")
        if not re.search(r"[@$!%*?&]", v):
            raise ValueError("Password must contain a special character (@$!%*?&)")

        return v


class EmployeeResponse(BaseModel):
    public_id:str
    firstName: str
    lastName: str
    email: EmailStr
    createdAt: datetime
