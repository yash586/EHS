from sqlmodel import Session, select
from config.db import engine
from models.observation_category import Category

def list_all():
    query = select(Category).where(Category.active == True)
    with Session(engine) as session:
        result = session.exec(query).fetchall()
        return result

def save(category: Category):
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

def getCategory(category_id:str):
    query = select(Category).where(Category.public_id == category_id, Category.active == True)
    with Session(engine) as session:
        result = session.exec(query).first()
        return result