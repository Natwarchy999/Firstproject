from fastapi import HTTPException
from bs4 import BeautifulSoup
from google import genai
from app.core.settings import settings
import os,shutil,requests,time
from app.core.db import LocalSession
from app.models.user_tasks import TaskModel
from app.core.security import create_access_token, verify_password, hash_password


# Register
def register_user(user ):
    db = LocalSession()
    existing_user = db.query(TaskModel).filter(
        TaskModel.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already registered"
        )

    new_user = TaskModel(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }

# Login
def login_user(form_data):
    db = LocalSession()

    db_user = db.query(TaskModel).filter(
        TaskModel.email == form_data.username
    ).first()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
        "message":"Login successfully"
    }

# logout
def logout_user():
    return {
        "message":"logout successfully"
    }

#delete account 
def delete_account(user):
 
    db=LocalSession()
    
    db_user=db.query(TaskModel).filter(
        TaskModel.email==user["sub"]
    ).first()

    db.delete(db_user)
    db.commit()

    return {
        "message ": "Account deleted successfull"
    }

#protected route 
def profile_access(user):
    return {
        'message': "Profile accessed successfully",
        'user': user
    }

#uploads file
UPLOAD_DIR="app/uploads"
def upload_file(file):
    filename=file.filename
    file_path=os.path.join(UPLOAD_DIR,filename)

    if not filename:
        raise HTTPException(status_code=400,detail="file not selected")

    os.makedirs(UPLOAD_DIR,exist_ok=True)

    with open(file_path,"wb") as buffer :
        shutil.copyfileobj(file.file,buffer)
    
    return {
        "message":"file upload successsfully ",
        "filename":filename,
        "file_url":f"http://127.0.0.8000/file={filename}"
    }

#read file
def get_file(filename):
    file_path=os.path.join(UPLOAD_DIR,filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404,detail="file not found ")
    
    return {
        "path":f"http://127.0.0.8000/files/{filename}",
        "file": file_path
    }

# 3rd party api
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# web crawling 
def get_news(request):
    url = "https://indianexpress.com/"

    header = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        )
    }

    response = requests.get(url, headers=header)

    print(response.status_code)

    title=[]
    soup = BeautifulSoup(response.text, "html.parser")


    for item in soup.find_all("a",class_="article-click topblockNews__sidebarLink"):
            title.append(item.get_text(strip=True))

    return {
        "news": title[:4]
    }

# pagination 
def pagination(page,limit):
    url="https://news.ycombinator.com/"
    header={
        "user_Agent":(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        )
    }
    response=requests.get(url,headers=header)
    print(response.status_code)

    soup=BeautifulSoup(response.text ,"html.parser")
    title=[]

    for item in soup.find_all("span" ,class_="titleline"):
        title.append(item.get_text(strip=True))

    # pagination logic
    start=(page-1)*limit
    end=start+limit

    return {
      "page":page,
      "limit":limit,
      "total":len(title),
      "data":title[start:end]
    }


#implement the caching 
cache_data=[]
last_fetch=0

def caching():

    global cache_data ,last_fetch

    start=time.time()
    if time.time() - last_fetch > 60:
        print("Fetching fresh Data")
        url="https://news.ycombinator.com/"
        header={
            "user_Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )
        }
        response=requests.get(url,headers=header)
        end=time.time()
        soup=BeautifulSoup(response.text ,"html.parser")

        cache_data=[
            item.text for item in soup.find_all("span" ,class_="titleline")
        ]
        last_fetch=time.time()
    else:
     print("Using cache data ")

     end=time.time()

     total_time=round(end-start,4)
     return {
        "time_taken":total_time,
        "data": cache_data[:5]
        }


# ai integration
client = genai.Client(api_key=settings.GEMINI_API_KEY)

def generate_new_quotes(prompt: str):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text

    