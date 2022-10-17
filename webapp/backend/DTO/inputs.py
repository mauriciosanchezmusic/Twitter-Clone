"""Inputs module."""
from pydantic import BaseModel

#from .inputs import UserInput, AdminInput

class UserInput(BaseModel):
    user_name : str
    hashed_password : str
    is_active : bool
    age : int
    name : str
    gender : str
    
class AdminInput(BaseModel):
    user_name : str
    hashed_password : str
    is_active : bool