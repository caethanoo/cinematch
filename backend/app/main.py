# Localização: app/main.py

import sys
from pathlib import Path

# Adiciona o diretório 'backend' ao caminho do Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI

# Importa as nossas rotas e configurações
from app.api.routes import users
from core.config import settings

# Importa a Base e o engine da nossa nova estrutura centralizada em 'app/db'
from app.db.base import Base
from app.db.session import engine

# --- ESTE É O BLOCO CORRETO PARA CRIAR AS TABELAS ---
# Ele usa a 'Base' que importámos diretamente para criar as tabelas.
# Não há mais 'models.Base' aqui.
Base.metadata.create_all(bind=engine)
# ----------------------------------------------------

# Cria a aplicação FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

# Endpoint raiz para um health check
@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao CineMatch API!"}

# Inclui as rotas de utilizadores na nossa aplicação
app.include_router(users.router, prefix="/users", tags=["users"])