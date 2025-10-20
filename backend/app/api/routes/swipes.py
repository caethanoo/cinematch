from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.swipe import SwipeCreate, SwipeInDB  # Importação direta
from app.api import deps
from app import crud

router = APIRouter()

@router.post("/", response_model=SwipeInDB)  # Usando importação direta
async def create_swipe(
    swipe: SwipeCreate,
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """Registra um novo swipe (like/dislike) em um filme"""
    return crud.create_swipe(db, swipe, current_user.id)

@router.get("/", response_model=List[SwipeInDB])
async def read_swipes(
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """Lista todos os swipes do usuário atual"""
    return crud.get_user_swipes(db, current_user.id)