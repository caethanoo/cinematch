# Localização: app/api/routes/users.py (VERSÃO COMPLETA E CORRETA)

from fastapi import APIRouter, Depends, HTTPException, status, Body 
from pydantic import ValidationError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm # Necessário para o /token

from app import crud, schemas, models # models é necessário para 'get_current_user' e 'User' no @router.get("/me")
from app.api import deps
from app.core.config import settings
from app.core import security 
# Necessário para criar e verificar tokens e senhas

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user(user_in: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    try:
        # Valida se o email já existe
        if crud.get_user_by_email(db, email=user_in.email):
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado"
            )
        
        # Tenta criar o usuário
        user = crud.create_user(db=db, user=user_in)
        return user
    
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db)
):
    """
    Autentica um utilizador e retorna um token de acesso.
    """
    # Passo 1: Autenticar o utilizador
    # Usamos o 'username' do formulário para procurar o e-mail na base de dados.
    user = crud.get_user_by_email(db, email=form_data.username)

    # Verificamos se o utilizador existe E se a senha está correta.
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        # Se não, lançamos um erro.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Passo 2: Se a autenticação for bem-sucedida, criar o token JWT.
    # Colocamos o e-mail do utilizador dentro do token.
    access_token = security.create_access_token(
        data={"sub": user.email}
    )

    # Passo 3: Retornar o token.
    # O padrão OAuth2 especifica que a resposta deve ser neste formato.
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.User)
def read_user_me(
    current_user: models.User = Depends(deps.get_current_user)
):
    """
    Obtém os dados do utilizador atual.
    """
    # A magia acontece na linha acima. Se o código chegar até aqui,
    # significa que o token é válido e o 'current_user' já foi carregado.
    return current_user