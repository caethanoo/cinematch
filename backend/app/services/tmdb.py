import httpx
from typing import List, Dict, Any
from app.core.config import settings

async def get_popular_movies() -> List[Dict[Any, Any]]:
    """
    Busca filmes populares na API do TMDB.
    
    Returns:
        List[Dict]: Lista de filmes populares com seus detalhes
    """
    url = f"https://api.themoviedb.org/3/movie/popular"
    
    headers = {
        "Authorization": f"Bearer {settings.TMDB_API_KEY}",
        "accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Lança exceção para status codes de erro
        
        data = response.json()
        return data.get("results", [])
    
    