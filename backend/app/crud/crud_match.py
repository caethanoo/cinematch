from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.swipe import Swipe
from typing import List, Dict
from app.services.tmdb import get_movie_details

async def get_user_matches(db: Session, user_id: int) -> List[Dict]:
    """
    Retorna filmes que receberam like do usuário e de outros usuários
    """
    # Pega os likes do usuário
    user_likes = db.query(Swipe).filter(
        and_(
            Swipe.user_id == user_id,
            Swipe.liked == True
        )
    ).all()
    
    matches = []
    for like in user_likes:
        # Busca outros usuários que curtiram o mesmo filme
        other_likes = db.query(Swipe).filter(
            and_(
                Swipe.movie_id == like.movie_id,
                Swipe.user_id != user_id,
                Swipe.liked == True
            )
        ).all()
        
        if other_likes:
            # Busca detalhes do filme
            movie = await get_movie_details(like.movie_id)
            matches.append({
                "movie_id": like.movie_id,
                "title": movie.get("title"),
                "matched_users": len(other_likes)
            })
    
    return matches