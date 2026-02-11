from fastapi import APIRouter, Query
from schemas.observation_schema import ObservationBase, ObservationResponse, ObservationUpdate
from services import observation_service
from typing import Annotated, List
router = APIRouter()

@router.post("/create", response_model=ObservationResponse)
def create_observation(item:ObservationBase):
    results = observation_service.new_observation(item)
    return results

@router.get("/view/{observation_id}", response_model=ObservationResponse)
def getObservation(observation_id:str):
    results = observation_service.getRecords(observation_id=observation_id)
    return results

@router.get("/list", response_model=List[ObservationResponse])
def listObservation(employee_id:int | None = None, category_id: int | None = None):
    results = observation_service.list_observation(employee_id, category_id)
    return results

@router.patch("/update/{observation_id}")
def update_observation(observation_id:str, item: ObservationUpdate):
    results = observation_service.update_observation(observation_id=observation_id, payload=item)
    return results

@router.delete("/delete/{observation_id}")
def delete_observation(observation_id:str):
    results = observation_service.delete_observation(observation_id=observation_id)
    return results