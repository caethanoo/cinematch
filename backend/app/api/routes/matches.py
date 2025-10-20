from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from app.api import deps
from app import crud, schemas
from app.crud import crud_match

router = APIRouter()

@router.get("/", response_model=List[dict])
async def get_matches(
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """Retorna lista de filmes que são matches"""
    return crud.get_user_matches(db, current_user.id)

@router.get("/recommended", response_model=List[dict])
async def get_recommendations(
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """Retorna filmes recomendados baseados nos swipes"""
    return await crud.get_recommendations(db, current_user.id)

@router.get("/stats")
async def get_match_statistics(
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """
    Retorna estatísticas dos matches do usuário
    """
    return await crud_match.get_match_statistics(db, current_user.id)

@router.get("/by-genre/{genre_id}")
async def get_matches_by_genre(
    genre_id: int,
    current_user = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """
    Filtra matches por gênero específico
    """
    matches = await crud_match.get_user_matches(db, current_user.id)
    return [
        match for match in matches
        if any(g["id"] == genre_id for g in match["genres"])
    ]