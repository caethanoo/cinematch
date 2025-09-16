# Localização: backend/app/main.py

from fastapi import FastAPI
from core.config import settings

# --- Configuração da Base de Dados ---
from app.db.base import Base
from app.db.session import engine

# --- Roteadores e Descoberta de Modelos ---
# Ao importar os roteadores abaixo, o Python irá seguir a cadeia de
# importações (routes -> deps -> crud -> models) e irá "descobrir"
# todos os nossos modelos (User, Swipe) automaticamente.
from app.api.routes import users, movies

# --- Criação das Tabelas ---
# Agora que os roteadores foram importados e os modelos "descobertos",
# podemos pedir ao SQLAlchemy para criar todas as tabelas encontradas.
Base.metadata.create_all(bind=engine)

# --- Criação da Aplicação ---
app = FastAPI(title=settings.PROJECT_NAME)

# --- Inclusão dos Roteadores ---
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo ao CineMatch API!"}