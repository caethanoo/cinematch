# Localização: backend/app/api/deps.py

from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app import models
from app.core.config import settings
from app.core.security import ALGORITHM
from app.db.session import SessionLocal

# Configuração do bearer token
security = HTTPBearer(
    scheme_name="Bearer",
    auto_error=True
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> models.User:
    try:
        # Log para debug
        print(f"Token recebido: {credentials.credentials[:10]}...")
        
        payload = jwt.decode(
            credentials.credentials,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        email: str = payload.get("sub")
        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido - email não encontrado"
            )
            
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado"
            )
            
        return user
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Falha na validação do token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )