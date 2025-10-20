# Localização: backend/app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- Schemas de Utilizador ---
class UserBase(BaseModel):
    email: EmailStr
    name: str # 'name' é um bom nome de campo

class UserCreate(UserBase):
    password: str

class UserPreferences(BaseModel):
    favorite_genres: List[int] = []
    language: str = "pt-BR"
    adult_content: bool = False

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    preferences: Optional[UserPreferences] = None

class User(UserBase):
    id: int
    is_active: bool = True # Geralmente os utilizadores são ativos por padrão
    preferences: Optional[UserPreferences] = None

    class Config:
        from_attributes = True # updated from orm_mode = True

# --- Schemas de Token (ADICIONADOS E CORRIGIDOS AQUI) ---
# Estas classes devem estar no mesmo nível que UserBase, UserCreate, User
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer" # "bearer" é o tipo padrão de token JWT

class TokenData(BaseModel):
    email: Optional[str] = None