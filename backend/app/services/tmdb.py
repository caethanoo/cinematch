# Localização: app/services/tmdb.py

import httpx
from typing import List, Dict, Any
from core.config import settings

TMDB_API_URL = "https://api.themoviedb.org/3"

# Melhoria no tipo de retorno: as chaves de um JSON são sempre strings.
async def get_popular_movies() -> List[Dict[str, Any]]:
    """
    Busca filmes populares na API do TMDB de forma assíncrona.
    """
    endpoint = f"{TMDB_API_URL}/movie/popular"
    
    # --- A CORREÇÃO ESTÁ AQUI ---
    # Em vez de 'headers', a API v3 espera a chave como um 'param' na URL.
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "pt-BR"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Passamos os parâmetros usando o argumento 'params'
            response = await client.get(endpoint, params=params)
            response.raise_for_status() # Lança exceção para erros (401, 404, etc.)
            
            data = response.json()
            return data.get("results", [])
        except httpx.HTTPStatusError as exc:
            print(f"Erro de HTTP ao chamar a API do TMDB: {exc.response.status_code}")
            return []
        except httpx.RequestError as exc:
            print(f"Ocorreu um erro de rede na requisição para o TMDB: {exc}")
            return []
        


if __name__ == "__main__":
    import asyncio
    from pprint import pprint

    
    async def main():
        print("A buscar filmes populares...")

     
        filmes = await get_popular_movies()

        if filmes:
            print(f"Encontrados {len(filmes)} filmes.")
            print("Aqui está o primeiro:")
            pprint(filmes[0]) # Agora 'filmes' é uma lista de verdade!
        else:
            print("Nenhum filme encontrado ou ocorreu um erro.")

   
    asyncio.run(main())