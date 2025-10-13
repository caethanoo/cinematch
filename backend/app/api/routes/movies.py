from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any
from app.api import deps
from app.services.tmdb import get_popular_movies, get_movie_details
from app.schemas.movie import MovieDetail

router = APIRouter()

@router.get("/next", response_model=List[Dict])
async def get_next_movies(
    current_user = Depends(deps.get_current_user)
):
    """
    Retorna próximos filmes para swipe.
    Requer autenticação via token JWT.
    """
    try:
        movies = await get_popular_movies()
        return movies[:10]  # Retorna 10 filmes
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar filmes: {str(e)}"
        )

@router.get("/{movie_id}", response_model=MovieDetail)
async def get_movie(
    movie_id: int,
    current_user = Depends(deps.get_current_user)
) -> Dict[str, Any]:
    """
    Retorna detalhes de um filme específico.
    
    Args:
        movie_id: ID do filme no TMDB
        current_user: Usuário autenticado (injetado via dependência)
    
    Returns:
        Detalhes do filme
        
    Raises:
        HTTPException: Se o filme não for encontrado ou houver erro na API
    """
    try:
        movie = await get_movie_details(movie_id)
        return movie
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Filme não encontrado: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar filme: {str(e)}"
        )