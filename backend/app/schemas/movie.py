from pydantic import BaseModel
from typing import List, Optional

class MovieDetail(BaseModel):
    id: int
    title: str
    overview: str
    poster_path: Optional[str] = None
    release_date: Optional[str] = None
    vote_average: Optional[float] = None
    genres: List[str] = []
    runtime: Optional[int] = None

class Genre(BaseModel):
    id: int
    name: str

class GenreList(BaseModel):
    genres: List[Genre]