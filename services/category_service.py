from  fastapi import HTTPException, status
from schemas.category_schema import CategoryBase, CategoryUpdateResponse
from models.observation_category import Category
from repository import category_repository


def list_categories():
    category = category_repository.list_all()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records")
    return category

def create_category(payload:CategoryBase):
    cats = Category(
        categoryName=payload.categoryName,
        categoryBackGround=payload.categoryBackGround
    )
    record = category_repository.save(cats)
    
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not created")
    return record

def update_category(category_id:str,payload:CategoryUpdateResponse):
    category = category_repository.getCategory(category_id=category_id)

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records")
    changes = payload.model_dump(exclude_unset=True)
    for key, value in changes.items():
        setattr(category,key,value)
    return category_repository.save(category)

def delete_category(category_id:str):
    category = category_repository.getCategory(category_id=category_id)

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Records")
    if category.active == False:
        return category
    category.active = True
    result = category_repository.save(category)
    return {"category_id": result.public_id, "message": "Deleted Successfully"}