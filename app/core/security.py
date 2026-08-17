from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import status,HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = "Natwat-chaudhary"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#hash password 
def hash_password(password: str):
    return pwd_context.hash(password)

#verify hashed password 
def verify_password(password:str,hashed_password:str):
    return pwd_context.verify(password,hashed_password)

#create token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

#verify token
def verify_access_token(token:dict):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:JWTError
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Token"
    )
        
