from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr 
    name : str
    
class UserCreate(UserBase):
    password: str   
    
class User(UserBase):
    id: int
    name : str
    
    class Config:
        from_attributes = True