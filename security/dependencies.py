from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from repository import employee_repository
from security.auth import SECRET_KEY, ALGO

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def current_user(token:str= Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGO])
        employee_id = payload.get("sub")

        if employee_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    employee = employee_repository.getByID(employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Employee Not found")
    
    return employee