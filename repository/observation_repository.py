from sqlmodel import Session, select
from config.db import engine
from models.observation_model import Observation

def _run_query(query, model=None, fetch_all=True, apply_active_filter=True):
    if apply_active_filter and model and hasattr(model, "active"):
        query = query.where(model.active == True)
    with Session(engine) as session:
        result = session.exec(query)
        return result.all() if fetch_all else result.first()


def save(observation: Observation):
    #Ensures session closes even if an exception occurs
    with Session(engine) as session: 
        session.add(observation)
        session.commit()
        session.refresh(observation)
        return observation
    
def getObservation(observation_id:str):
    query = select(Observation).where(Observation.public_id == observation_id)
    results = _run_query(query=query, fetch_all=False)
    return results

def get_by_employee(employeeid:int):
    query = select(Observation).where(Observation.employee_id == employeeid)
    results = _run_query(query=query)
    return results

def get_by_category(categoryid:int):
    query = select(Observation).where(Observation.category_id == categoryid)
    results = _run_query(query=query)
    return results

def findAll():
    results = _run_query(query=select(Observation))
    return results