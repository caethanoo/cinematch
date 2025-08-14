from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from fastapi.security import OAuth2PasswordRequestForm
from core import security
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate
):
    # 1. Verifica se o utilizador já existe no banco de dados.
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        # Se existir, lança uma exceção HTTP, que o FastAPI converterá numa resposta de erro.
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    # 2. Se não existir, chama a nossa função CRUD para criar o utilizador.
    user = crud.create_user(db, user_in=user_in)
    return user

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