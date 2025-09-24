#aqui nesse arquivo eu vou gerir as senhas e gerir sessões
from datetime import datetime, timedelta, UTC
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.core.config import settings
from fastapi import HTTPException, status

# Configuração do contexto de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Constantes
ALGORITHM = "HS256"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto corresponde ao hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Gera um hash para a senha"""
    return pwd_context.hash(password)

def create_access_token(data: dict) -> str:
    """Cria um token JWT"""
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Adicione log para debug
    print(f"Gerando token com payload: {to_encode}")
    
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=ALGORITHM
    )
    return encoded_jwt

def decode_access_token(token: str) -> str:
    """
    Decodifica o token de acesso JWT.
    Raises:
        HTTPException: Se o token for inválido ou expirado
    """
    try:
        # Log para debug
        print(f"Tentando decodificar token: {token[:10]}...")
        
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
        
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return email
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Erro na validação do token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )



