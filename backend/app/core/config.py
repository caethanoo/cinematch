from pydantic_settings import BaseSettings
import os
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from core.config import settings 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Settings(BaseSettings):
   
    PROJECT_NAME: str
    PROJECT_VERSION: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8' 


settings = Settings()


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # O token valerá por 30 minutos

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


