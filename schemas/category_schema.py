from pydantic import BaseModel, Field
from datetime import datetime

class CategoryBase(BaseModel):
    categoryName: str = Field(min_length=1)
    categoryBackGround: str | None = None

class CategoryResponse(CategoryBase):
    public_id: str
    createdAt: datetime
    active: bool

class CategoryUpdateResponse(BaseModel):
    categoryName: str | None = None
    categoryBackGround: str | None = None