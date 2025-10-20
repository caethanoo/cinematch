# Localização: app/crud/crud_swipe.py
from sqlalchemy.orm import Session
from app.models.swipe import Swipe
from app.schemas.swipe import SwipeCreate
from typing import List

def create_swipe(db: Session, swipe: SwipeCreate, user_id: int) -> Swipe:
    """
    Cria um novo swipe no banco de dados
    """
    db_swipe = Swipe(
        movie_id=swipe.movie_id,
        liked=swipe.liked,
        user_id=user_id
    )
    db.add(db_swipe)
    db.commit()
    db.refresh(db_swipe)
    return db_swipe

def get_user_swipes(db: Session, user_id: int) -> List[Swipe]:
    """
    Retorna todos os swipes de um usuário específico
    """
    return db.query(Swipe).filter(Swipe.user_id == user_id).all()