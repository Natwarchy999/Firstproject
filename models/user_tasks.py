from sqlalchemy import Column, Integer, Boolean, String
from database.db import Base

class TaskModel(Base):
    __tablename__="user_tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True,index=True)
    password = Column(String(255))
    title = Column(String(255))
    description = Column(String(500))
    is_completed = Column(Boolean, default=False)
