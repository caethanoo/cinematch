# Localização: backend/app/api/deps.py

from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app import models
from app.core.config import settings
from app.core.security import ALGORITHM
from app.db.session import SessionLocal

# Definimos o OAuth2PasswordBearer aqui, com o tokenUrl correto e relativo
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="users/token",
    scheme_name="Bearer"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> models.User:
    try:
        # Adicione log para debug
        print(f"Tentando decodificar token: {token[:10]}...")
        
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        print(f"Payload decodificado: {payload}")
        
        email: str = payload.get("sub")
        if not email:
            raise JWTError("Email não encontrado no token")
            
        # Busca usuário no banco
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise JWTError("Usuário não encontrado")
            
        return user
        
    except JWTError as e:
        print(f"Erro ao validar token: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Não foi possível validar credenciais: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )