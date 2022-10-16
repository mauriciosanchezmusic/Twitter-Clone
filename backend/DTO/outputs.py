"""Outputs module."""
from pydantic import BaseModel

#from .outputs import UserOutput, AdminOutput

class UserOutput(BaseModel):
    user_name : str
    age : int
    name : str
    gender : str
    
class AdminOutput(BaseModel):
    user_name : str