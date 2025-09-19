# Localização: app/services/tmdb.py

import httpx
from typing import List, Dict, Any
from app.core.config import settings

TMDB_API_URL = "https://api.themoviedb.org/3"

# Melhoria no tipo de retorno: as chaves de um JSON são sempre strings.
async def get_popular_movies() -> List[Dict[str, Any]]:
    """
    Busca filmes populares na API do TMDB de forma assíncrona.
    """
    endpoint = f"{TMDB_API_URL}/movie/popular"
    
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "pt-BR",
        "page": 1
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(endpoint, params=params)
            response.raise_for_status()
            
            data = response.json()
            movies = data.get("results", [])
            
            # Log para debug
            print(f"Status: {response.status_code}")
            print(f"Filmes encontrados: {len(movies)}")
            
            return movies
        except Exception as e:
            print(f"Erro: {e}")
            return []

if __name__ == "__main__":
    import asyncio
    
    async def main():
        print("Buscando filmes populares...")
        filmes = await get_popular_movies()
        
        for filme in filmes[:5]:  # Mostra apenas os 5 primeiros
            print("\n" + "="*50)
            print(f"Título: {filme['title']}")
            print(f"Nota: {filme['vote_average']}")
            print(f"Data de Lançamento: {filme['release_date']}")
    
    asyncio.run(main())