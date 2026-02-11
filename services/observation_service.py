from repository import observation_repository
from schemas.observation_schema import ObservationBase, ObservationResponse, ObservationUpdate
from models.observation_model import Observation
from datetime import datetime
from exceptions.observation_exceptions import ObservationNotCreated, ObservationNotFoundError

def getRecords(observation_id:str):
    obs = observation_repository.getObservation(observation_id=observation_id)
    if not obs:
        raise ObservationNotFoundError("Record does not exists")
    return obs

def new_observation(payload: ObservationBase):
    obs = Observation(
        title=payload.title,
        category_id=payload.category_id,
        employee_id=payload.employee_id,
        location=payload.location,
        date= payload.date
    )
    observation = observation_repository.save(obs)

    if not observation:
        raise ObservationNotCreated("Observation not created")
    
    return observation

def list_observation(employee_id: int | None = None, category_id: int | None = None):
    if employee_id is not None:
        return observation_repository.get_by_employee(employee_id)
    if category_id is not None:
        return observation_repository.get_by_category(category_id)
    return observation_repository.findAll()

def update_observation(observation_id:str, payload:ObservationUpdate):
    observation = observation_repository.getObservation(observation_id=observation_id)

    if not observation:
        raise ObservationNotFoundError("Observation Not found")
    
    changes = payload.model_dump(exclude_unset=True)
    for key, value in changes.items():
        setattr(observation, key, value)
    return observation_repository.save(observation)

def delete_observation(observation_id:str):
    observation = observation_repository.getObservation(observation_id=observation_id)
    
    if not observation:
        raise ObservationNotFoundError("Observation Not found")
    if observation.active == False:
        return observation

    observation.active = False
    obs = observation_repository.save(observation)
    return {"observation_id":obs.public_id, "message": "Deleted Successfully"}