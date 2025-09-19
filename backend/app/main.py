# Localização: backend/app/main.py

from fastapi import FastAPI
from app.core.config import settings  # Corrigido o caminho de importação

# --- Configuração da Base de Dados ---
from app.db.base import Base
from app.db.session import engine

# --- Roteadores ---
from app.api.routes import users, movies

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Criar app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Incluir routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo ao CineMatch API!"}