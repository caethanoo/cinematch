from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    preferences = Column(JSON, nullable=True)
    
    swipes = relationship("Swipe", back_populates="user")

