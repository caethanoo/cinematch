from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/")
async def get_swipes(
    db: Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    """
    Recupera os swipes do usuário atual
    """
    return {"message": "Endpoint de swipes funcionando"}

@router.post("/")
async def create_swipe(
    swipe: schemas.SwipeCreate,
    db: Session = Depends(deps.get_db),
    current_user = Depends(deps.get_current_user)
):
    """
    Cria um novo swipe para o usuário atual
    """
    return {"message": "Swipe criado com sucesso"}