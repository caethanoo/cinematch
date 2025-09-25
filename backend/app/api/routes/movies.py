from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.api import deps
from app import models

router = APIRouter()

@router.get("/next", response_model=List[Dict[str, Any]])
async def get_next_movies(
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db)
):
    """
    Retorna próximos filmes para o usuário fazer swipe
    Requer autenticação.
    """
    try:
        # Aqui você pode adicionar sua lógica para buscar filmes
        # Por enquanto, retornamos uma resposta de teste
        return [
            {
                "id": 1,
                "title": "Filme Teste",
                "overview": "Descrição do filme"
            }
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )