# Localização: app/schemas/__init__.py

# Exporta os schemas do ficheiro user.py
from .user import User, UserCreate, UserUpdate, UserPreferences, Token

# Exporta os schemas do ficheiro movie.py
from .movie import MovieDetail

# Exporta os schemas do ficheiro swipe.py
from .swipe import SwipeCreate, SwipeInDB

__all__ = [
    "User",
    "UserCreate",
    "UserUpdate",
    "UserPreferences",
    "Token",
    "MovieDetail",
    "SwipeCreate",
    "SwipeInDB"
]