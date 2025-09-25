from pydantic import BaseModel

class SwipeBase(BaseModel):
    """Schema base com campos comuns"""
    movie_id: int
    liked: bool

class SwipeCreate(SwipeBase):
    """Schema usado para criar um novo swipe"""
    pass

class Swipe(SwipeBase):
    """Schema completo com dados retornados do banco"""
    id: int
    user_id: int

    class Config:
        from_attributes = True