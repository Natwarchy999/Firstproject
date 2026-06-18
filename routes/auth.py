from fastapi import APIRouter
from schemas.user import UserCreate ,UserLogin
from services.auth_service import login_user,register_user,logout_user


router = APIRouter()

@router.get("/")
def root():
    return{"api is running "}

@router.post("/register")
def register(user:UserCreate):
    return register_user(user)


@router.post("/login")
def login(user:UserLogin):
    return login_user(user)

@router.post("/logout")
def logout():
    return logout_user()

