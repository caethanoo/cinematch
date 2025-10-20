from pydantic import BaseModel

class SwipeBase(BaseModel):
    movie_id: int
    liked: bool

class SwipeCreate(SwipeBase):
    pass

class SwipeInDB(SwipeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True