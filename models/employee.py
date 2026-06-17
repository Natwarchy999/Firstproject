from sqlalchemy import Column,INTEGER,String,Boolean,Float
from database.db import Base

class EmployeeDetails(Base):
    __tablename__="employee"

    id = Column(INTEGER ,primary_key=True)
    name = Column(String(100))
    dept = Column(String(50))
    salary = Column(Float)


