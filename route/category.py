from fastapi import APIRouter, HTTPException, status
from schemas.category_schema import CategoryBase, CategoryResponse, CategoryUpdateResponse
from services import category_service
from typing import List

router = APIRouter()

@router.get("/list", response_model=List[CategoryResponse])
def lists():
    results = category_service.list_categories()
    return results

@router.post("/create", response_model=CategoryResponse)
def create(payload:CategoryBase):
    results = category_service.create_category(payload=payload)
    return results

@router.patch("/update/{category_id}")
def update(category_id:str, payload: CategoryUpdateResponse):
    if not category_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Category Id missing")
    results = category_service.update_category(category_id=category_id, payload=payload)
    return results

@router.delete("/delete/{category_id}")
def delete(category_id:str):
    if not category_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Category Id missing")
    results = category_service.delete_category(category_id=category_id)
    return results