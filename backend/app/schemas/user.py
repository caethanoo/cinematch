# Localização: backend/app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional # Mantenha se estiver a ser usado, caso contrário pode remover
# constr não está a ser usado nos schemas que me enviou, pode remover se não o for usar.

# --- Schemas de Utilizador ---
class UserBase(BaseModel):
    email: EmailStr
    name: str # 'name' é um bom nome de campo

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True # Geralmente os utilizadores são ativos por padrão

    class Config:
        from_attributes = True # updated from orm_mode = True

# --- Schemas de Token (ADICIONADOS E CORRIGIDOS AQUI) ---
# Estas classes devem estar no mesmo nível que UserBase, UserCreate, User
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer" # "bearer" é o tipo padrão de token JWT

class TokenData(BaseModel):
    # 'username' é muitas vezes o email quando se usa OAuth2PasswordBearer
    username: str | None = None