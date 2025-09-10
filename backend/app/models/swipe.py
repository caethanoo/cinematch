from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Swipe(Base):
    """
    Modelo para registrar as interações (swipes) dos usuários com filmes
    """
    __tablename__ = "swipes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    liked = Column(Boolean, nullable=False)

    # Relacionamento com o usuário (opcional, mas útil)
    user = relationship("User", back_populates="swipes")