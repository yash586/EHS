from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL, echo=True)
from models.observation_category import Category
from models.observation_employee import Employee
from models.observation_model import Observation
def get_session():
    with Session(engine) as session:
        yield session