from security.password import verify_password, hash_password
from security.auth import create_access_token
from  fastapi import HTTPException, status, Depends
from repository import employee_repository
from schemas.employee_schema import EmployeeBase, EmployeeResponse
from models.observation_employee import Employee 

def login(email:str, password:str):
    employee = employee_repository.getEmail(email=email)
    if not employee:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    if not verify_password(password=password, hashed_password=employee.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    token = create_access_token({"email":employee.email, "sub":employee.public_id})
    return {"access_token":token, "token_type":"bearer"}

def signup(payload: EmployeeBase):
    existing = employee_repository.getEmail(payload.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Already Email Registered")
    
    create_employee = Employee(
        firstName=payload.firstName,
        lastName=payload.lastName,
        email=payload.email,
        password=hash_password(payload.password)
    )
    return employee_repository.createEmployee(create_employee)