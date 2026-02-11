from fastapi import APIRouter, Form, HTTPException,status
from services import employee_service
from schemas import employee_schema

router = APIRouter()

@router.post("/signup", response_model=employee_schema.EmployeeResponse, status_code=200)
def signup(payload:employee_schema.EmployeeBase):
    results = employee_service.signup(payload=payload)
    return results

@router.post("/login")
def login(email:str = Form(), password:str = Form()):

    if not email or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email and Password are mandatory")
    results = employee_service.login(email=email, password=password)
    return results