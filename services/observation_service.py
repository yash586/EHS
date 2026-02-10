from repository import observation_repository
from schemas.observation_schema import ObservationBase, ObservationResponse
from models.observation_model import Observation
from datetime import datetime
from exceptions.observation_exceptions import ObservationNotCreated, ObservationNotFoundError

# def get_by_id(observation_id:int):
#     observation = observation_repository.find_by_id(observation_id=observation_id)

#     if not observation:
#         return {"message": "Not Found"}
    
#     return observation
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
    observation = observation_repository.create_observation(obs)

    if not observation:
        raise ObservationNotCreated("Observation not created")
    
    return observation

def list_observation(employee_id: int | None = None, category_id: int | None = None):
    if employee_id is not None:
        return observation_repository.get_by_employee(employee_id)
    if category_id is not None:
        return observation_repository.get_by_category(category_id)
    return observation_repository.findAll()


# def update(observation_id:int, payload:ObservationUpdate):
#     observation = observation_repository.find_by_id(observation_id=observation_id)
    
#     if not observation:
#         raise ObservationNotFoundError("Observation not found")
    
#     if observation.get("status") == ObservationStatus.closed:
#         raise ObservationClosedError("Cannot update a closed observation")
    
#     changes = payload.model_dump(exclude_unset=True)
#     updated = observation_repository.update_observation(observation_id, changes)
#     return updated

# def delete(observation_id:int):
#     observation = observation_repository.find_by_id(observation_id=observation_id)
#     if not observation:
#         raise ObservationNotFoundError("Observation not found")
#     result = observation_repository.delete(observation_id=observation_id)
#     return result

# def getBySeverity(severity:Severity):
#     observation = observation_repository.find_by_severity(severity.value)
#     if not observation:
#         raise ObservationNotFoundError("Observation not found")
#     return observation