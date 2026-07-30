from fastapi import HTTPException
import os,shutil
from app.core.db import LocalSession
from app.models.user_tasks import TaskModel
from app.core.security import create_access_token, verify_password, hash_password


# Register
def register_user(user):
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

#logout
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

#fetch backend data 
def fetch_api():
    return {
        "message ": "fetching successfull"
    }
