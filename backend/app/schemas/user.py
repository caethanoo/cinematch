from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr 
    name: str

class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True