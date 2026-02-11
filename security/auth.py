from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRES_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES")

def create_access_token(data:dict, expires_delta:timedelta | None = None):
    encodeData = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=float(ACCESS_TOKEN_EXPIRES_MINUTES)))
    encodeData.update({"exp": expire})
    encoded_jwt = jwt.encode(encodeData, key=SECRET_KEY, algorithm=ALGO)
    return encoded_jwt

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGO])
        return payload
    except JWTError:
        return None
