from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    print(f"Criando usuário: {user.dict()}")
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=get_password_hash(user.password)  # Hash da senha
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()  # Desfaz alterações em caso de erro
        raise e

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def update_preferences(db: Session, user_id: int, preferences: schemas.UserPreferences):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    db_user.preferences = preferences.model_dump()
    db.commit()
    db.refresh(db_user)
    return db_user

