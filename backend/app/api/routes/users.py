# Localização: app/api/routes/users.py (VERSÃO TEMPORÁRIA DE TESTE)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas # Nao importamos 'models' aqui diretamente
from app.api import deps # Onde está get_db

router = APIRouter()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate # <--- Este é o único parâmetro de dados do corpo
):
    # 1. Verifica se o utilizador já existe no banco de dados.
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        # Se existir, lança uma exceção HTTP.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, # Use status.HTTP_400_BAD_REQUEST para consistência
            detail="The user with this email already exists in the system.",
        )

    # 2. Se não existir, cria o utilizador.
    # Lembra-se que o CRUD espera 'user', então passamos user_in para 'user'.
    new_user = crud.create_user(db=db, user=user_in)
    return new_user

# REMOVEMOS TEMPORARIAMENTE AS ROTAS DE LOGIN E DE 'GET ME' PARA ISOLAR O PROBLEMA.
# Elas serão adicionadas de volta depois que o endpoint de criação de usuário funcionar.