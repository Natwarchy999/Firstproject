from fastapi import APIRouter, Depends,UploadFile,File,Request
from app.dependencies.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate,PromptRequest
from app.services.auth_service import login_user, register_user, logout_user, delete_account, profile_access,upload_file,get_file,get_posts,get_news,pagination,caching,generate_new_quotes
from app.dependencies.limiter import limiter


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
def get_f(filename:str):
    return get_file(filename)

@router.get("/posts")
def get_p():
    return get_posts()

@router.get("/news")
@limiter.limit("5/minutes")
def news(request:Request):
    return get_news(request)

@router.get("/bulk_news")
def bulk_news(page: int=1 ,limit:int=5):
    return pagination(page,limit)

@router.get("/cache")
def cache():
    return caching()



# ai generation 
@router.post("/generate_qoutes")
def generate_qoutes(data:PromptRequest):

    result=generate_new_quotes(data.prompt)
    return {
        "success":True,
        "response":result
    }
