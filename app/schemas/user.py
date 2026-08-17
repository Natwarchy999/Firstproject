from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str

class PromptRequest(BaseModel):
    prompt:str 

