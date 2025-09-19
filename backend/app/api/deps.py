from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from app.db.session import SessionLocal
from app import crud, models
from app.core.config import settings

# Esta linha cria um "esquema" de segurança.
# Ela diz ao FastAPI: "Para te autenticares, espero um token na URL '/users/token'".
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.User:
    """
    Dependência para obter o utilizador atual a partir do token JWT.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Usa a nossa nova função para ler o token
    email = security.decode_access_token(token)
    if email is None:
        raise credentials_exception

    # Vai à base de dados buscar o utilizador correspondente a esse e-mail
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

    return user