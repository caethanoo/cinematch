# Localização: app/api/routes/swipes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Swipe)
def register_swipe(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    swipe_in: schemas.SwipeCreate
):
    """
    Regista um novo swipe (like/dislike) para o utilizador logado.
    """
    # Chama a função CRUD que acabámos de criar
    swipe = crud.create_swipe(db=db, swipe_in=swipe_in, user_id=current_user.id)
    return swipe