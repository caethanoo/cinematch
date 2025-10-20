# Localização: app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.user import User
from app.models.swipe import Swipe