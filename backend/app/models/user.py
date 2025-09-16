from sqlalchemy import Column, Integer, String, Boolean
# Importamos a nossa Base centralizada!
from app.db.base import Base

from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    swipes = relationship("Swipe", back_populates="owner")
    
