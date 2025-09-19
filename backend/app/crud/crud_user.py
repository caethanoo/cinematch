from sqlalchemy.orm import Session
from app.models import user as models  
from app.schemas import user as schemas
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

