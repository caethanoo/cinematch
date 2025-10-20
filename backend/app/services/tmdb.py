# Localização: app/services/tmdb.py

from typing import List, Dict, Any
import httpx
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

async def get_movie_details(movie_id: int) -> Dict[str, Any]:
    """
    Busca detalhes de um filme específico na API do TMDB.
    """
    endpoint = f"{TMDB_API_URL}/movie/{movie_id}"
    
    # Corrigido: Usando api_key como parâmetro de query
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "pt-BR"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(endpoint, params=params)
            
            # Debug log
            print(f"Status: {response.status_code}")
            print(f"URL: {response.url}")
            
            response.raise_for_status()
            data = response.json()
            
            return {
                "id": data["id"],
                "title": data["title"],
                "overview": data.get("overview", ""),
                "poster_path": data.get("poster_path"),
                "release_date": data.get("release_date"),
                "vote_average": data.get("vote_average"),
                "genres": [genre["name"] for genre in data.get("genres", [])],
                "runtime": data.get("runtime")
            }
            
        except httpx.HTTPStatusError as e:
            print(f"Erro na requisição: {str(e)}")
            raise ValueError(f"Erro ao buscar filme: {str(e)}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise ValueError(f"Erro inesperado: {e}")

async def get_genres() -> List[dict]:
    """
    Busca lista de gêneros disponíveis na API do TMDB.
    """
    endpoint = f"{TMDB_API_URL}/genre/movie/list"
    
    headers = {
        "Authorization": f"Bearer {settings.TMDB_API_KEY}",
        "accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                endpoint,
                headers=headers,
                params={"language": "pt-BR"}
            )
            response.raise_for_status()
            
            data = response.json()
            return data.get("genres", [])
            
        except Exception as e:
            print(f"Erro ao buscar gêneros: {e}")
            return []

async def search_movies(query: str, genre_id: int = None, page: int = 1) -> dict:
    """
    Busca filmes por título e opcionalmente filtra por gênero
    """
    endpoint = f"{TMDB_API_URL}/search/movie"
    
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "pt-BR",
        "query": query,
        "page": page
    }
    
    if genre_id:
        params["with_genres"] = genre_id
    
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

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