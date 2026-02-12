from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from route.observation import router as observation_router
from route.employee import router as employee_router
from route.category import router as category_router
from exceptions.handlers import observation_not_found,observation_status_error, observation_create_error
from exceptions.observation_exceptions import ObservationClosedError, ObservationNotFoundError, ObservationNotCreated
from sqlmodel import SQLModel
from config.db import engine
from security.dependencies import current_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating the databases")
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="Safety Observation Api", lifespan=lifespan)

app.include_router(
    observation_router,
    prefix="/api/observations",
    tags=["Observations"],
    dependencies=[Depends(current_user)]
)

app.include_router(
    category_router,
    prefix="/api/category",
    tags=["Category"],
    dependencies=[Depends(current_user)]
)

app.include_router(
    employee_router,
    prefix="/api",
    tags=["Employee"]
)

app.add_exception_handler(ObservationNotFoundError, observation_not_found)
app.add_exception_handler(ObservationClosedError, observation_status_error)
app.add_exception_handler(ObservationNotCreated, observation_create_error)
