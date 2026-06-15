from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app =FastAPI()

# Temporary storage
users = {}

# Request Models

class RegisterUser(BaseModel):
    name:str
    email:str
    password:str

class LoginUser(BaseModel):
    email:str
    password:str   


@app.get("/")
def root():
    return {"The Api is running "}


# Register
@app.post("/register")
def Register(user : RegisterUser):

    if user.email in users :
        raise HTTPException(
             status_code=400,
             detail="Email already registered"
            )
         
    
    users[user.email]={
        "name": user.name,
        "password": user.password
    }

    return {"user Registered successfully"}


# Login
@app.post("/login")
def Login(user : LoginUser):

    if user.email not in users:

        raise HTTPException(
            status_code=404,
            detail="user not found "
        )
    
    if users[user.email]['password'] != user.password:
        raise HTTPException(
            status_code=400,
            detail="incorrect password"
        )
    
    return {"login successfully "}
    

# Logout
@app.post("/logout")
def Logout():
    return {
        "message":"logout successfully"
    }
