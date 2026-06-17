from fastapi import FastAPI, HTTPException
from database.db import Base, engine
from models.user_tasks import TaskModel
from models.employee import EmployeeDetails
from schemas.user import RegisterUser,LoginUser
from database.db import LocalSession

Base.metadata.create_all(engine)

app = FastAPI(title="this is for creating table")

@app.get("/")
def root():
    return {"The Api is running "}

# Register
@app.post("/register")
def Register(user: RegisterUser):

    db = LocalSession()

    existing_user = db.query(TaskModel).filter(
        TaskModel.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = TaskModel(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "id": new_user.id
    }


 # Login
@app.post("/login")
def Login(user: LoginUser):

    db = LocalSession()

    db_user = db.query(TaskModel).filter(
        TaskModel.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if db_user.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    return {
        "message": "Login successful"
    }

# Logout
@app.post("/logout")
def Logout():
    return {
        "message":"logout successfully"
    }
