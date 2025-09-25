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

security = HTTPBearer(
    scheme_name="Bearer",
    description="Digite 'Bearer' seguido do seu token JWT",
    auto_error=True
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> models.User:
    """
    Valida o token JWT e retorna o usuário atual.
    
    Raises:
        HTTPException: Se o token for inválido ou o usuário não existir
    """
    try:
        # Extrai o token das credenciais
        token = credentials.credentials
        
        # Decodifica o token
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        # Extrai o email do token
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido - email não encontrado",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        # Busca o usuário no banco
        user = db.query(models.User).filter(models.User.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return user
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Erro na validação do token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )