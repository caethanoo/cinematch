# Localização: backend/app/api/deps.py

from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer # <--- DEVE ESTAR AQUI!
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import models, schemas
from app.db.session import SessionLocal
from app.core import security # Certifique-se que é app.core
from app.core.config import settings # Certifique-se que é app.core

# Definimos o OAuth2PasswordBearer aqui, com o tokenUrl correto e relativo
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="users/token",
    scheme_name="JWT"  # Nome que aparecerá no Swagger UI
) # <--- AQUI ESTÁ A CHAVE!

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) # O token é injetado pelo OAuth2PasswordBearer
) -> models.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica o token JWT
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, # A SECRET_KEY do seu config.py
            algorithms=[security.ALGORITHM],
            options={"verify_aud": False} # Pode ser necessário ajustar se tiver AUD
        )
        # O 'sub' (subject) deve ser o e-mail do utilizador
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except (JWTError, ValidationError):
        raise credentials_exception

    # Busca o utilizador na base de dados
    user = db.query(models.User).filter(models.User.email == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user