from fastapi import HTTPException
from database.db import LocalSession
from models.user_tasks import TaskModel


#Register 
def register_user(user):

    db = LocalSession()

    existing_user=db.query(TaskModel).filter(
        TaskModel.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="user already Registered"
        )
    
    new_user=TaskModel(
        name =user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
     
    return{
        "message":"user Registered successfully "
    }

#Login 
def login_user(user):
    db=LocalSession()

    db_user=db.query(TaskModel).filter(
        TaskModel.email==user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if db_user.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="incorrect password "
        )
    
    return {
        "message ": "Login Successfully "
    }

#logout
def logout_user():
    return {
        "message":"logout successfully"
    }