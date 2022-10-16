"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer

from ..database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    age = Column(Integer)
    name = Column(String)
    gender = Column(String)
               
class Admin(Base):

    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
