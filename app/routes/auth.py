from fastapi import APIRouter, Depends,UploadFile,File
from app.dependencies.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate
from app.services.auth_service import login_user, register_user, logout_user, delete_account, profile_access,upload_file,get_file,fetch_api



router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    return register_user(user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data)

@router.post("/logout")
def logout():
    return logout_user()

@router.delete("/delete_account")
def delete_user_account(user=Depends(get_current_user)):
    return delete_account(user)

@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return profile_access(current_user)

@router.post("/upload_file")
def upload(file: UploadFile=File(...)):
    return upload_file(file)

@router.get("/get_file={filename}")
def get(filename:str):
    return get_file(filename)

@router.get("/fetch")
def fetch():
    return fetch_api();
