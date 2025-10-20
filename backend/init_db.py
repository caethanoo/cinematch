
from app.db.base import Base
from app.db.session import engine
from app import models

print("Criando tabelas do banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")

