from sqlalchemy.orm import Session
from app.models import user as models  
from app.schemas import user as schemas

def get_user_by_email(db: Session, email: str):
   
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.User):
   
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
    