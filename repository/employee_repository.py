from sqlmodel import Session, select
from config.db import engine
from models.observation_employee import Employee

def getEmail(email:str):
    query = select(Employee).where(Employee.email == email)
    with Session(engine) as session:
        result = session.exec(query).first()
        return result
    
def createEmployee(employee: Employee):
    with Session(engine) as session:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee
