#aqui nesse arquivo eu vou gerir as senhas e gerir sessões
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACESS_TOKEN_EXPIRE_MINUTES: int = 30
ALGORITHM = "HS256"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> str | None:
    """
    Decodifica o token de acesso para obter o e-mail do utilizador (o 'sub').
    """
    try:
        # Tenta decodificar o token usando a nossa chave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extrai o e-mail do campo 'sub' (subject)
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        # Se o token for inválido (assinatura errada, expirado, etc.), retorna None
        return None



