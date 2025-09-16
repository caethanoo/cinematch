# Localização: app/api/routes/movies.py

from fastapi import APIRouter, Depends
import random # Vamos usar para escolher um filme aleatório

# Importamos as nossas ferramentas e o novo serviço
from app.api import deps
from app import models, services
from app.services import tmdb # Importamos especificamente o nosso serviço TMDB

router = APIRouter()

@router.get("/next", response_model=dict)
async def get_next_movie_for_swipe(
    # AQUI ESTÁ A MAGIA:
    # Ao adicionar esta dependência, garantimos que só utilizadores logados
    # podem aceder a este endpoint. Se o token for inválido, o acesso é barrado.
    current_user: models.User = Depends(deps.get_current_user)
):
    """
    Busca um filme aleatório da lista de populares do TMDB para o utilizador dar swipe.
    """
    # 1. Usamos o nosso serviço para buscar a lista de filmes populares.
    popular_movies = await tmdb.get_popular_movies()
    
    # 2. Se a lista não estiver vazia, escolhemos um filme aleatoriamente.
    if popular_movies:
        random_movie = random.choice(popular_movies)
        return random_movie
    
    # 3. Se a lista estiver vazia ou ocorrer um erro, retornamos uma mensagem.
    return {"message": "Não foi possível buscar filmes no momento."}