# Localização: app/crud/crud_swipe.py
from sqlalchemy.orm import Session
from app import models, schemas

def create_swipe(db: Session, swipe_in: schemas.SwipeCreate, user_id: int) -> models.Swipe:
    # Cria um objeto do modelo Swipe com os dados recebidos
    db_swipe = models.Swipe(
        movie_id=swipe_in.movie_id,
        liked=swipe_in.liked,
        user_id=user_id  # Associa o swipe ao utilizador logado
    )
    db.add(db_swipe)
    db.commit()
    db.refresh(db_swipe)
    return db_swipe