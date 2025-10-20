# 📚 Guia de Estudo - Backend CineMatch

## 🔧 Tecnologias Principais

### FastAPI
- Framework web assíncrono e moderno
- Documentação automática (Swagger/OpenAPI)
- Validação com Pydantic
- Alta performance e tipagem

**O que estudar:**
- Rotas e decoradores
- Sistema de dependências
- Schemas Pydantic
- Middleware e CORS

### SQLAlchemy
- ORM para Python
- Gerenciamento de banco de dados
- Mapeamento objeto-relacional

**Conceitos principais:**
- Models e relacionamentos
- Sessões e queries
- Migrations e versionamento

### JWT (JSON Web Tokens)
- Autenticação e autorização
- Implementação com python-jose
- Segurança da API

**Pontos importantes:**
- Estrutura do token
- Payload e claims
- Boas práticas de segurança

## 📁 Estrutura do Projeto

### `/app/models/`
Definição das tabelas do banco:
- `user.py`: Modelo de usuário
- `swipe.py`: Modelo de interações

### `/app/schemas/`
Validação de dados (Pydantic):
- `user.py`: Schemas de usuário
- `movie.py`: Schemas de filmes
- `swipe.py`: Schemas de interações

### `/app/crud/`
Operações no banco:
- `crud_user.py`: Operações de usuário
- `crud_swipe.py`: Operações de swipes

### `/app/api/routes/`
Endpoints da API:
- `users.py`: Rotas de usuário
- `movies.py`: Rotas de filmes
- `swipes.py`: Rotas de interações

## 🔄 Fluxo de Requisições

1. Cliente faz requisição
2. Route processa request
3. Schema valida dados
4. CRUD executa operação
5. Model interage com banco
6. Resposta retorna ao cliente

## 📚 Recursos de Aprendizado

### FastAPI
- [Documentação Oficial](https://fastapi.tiangolo.com)
- Tutoriais interativos
- Exemplos práticos

### SQLAlchemy
- [Documentação](https://docs.sqlalchemy.org)
- Tutoriais básicos/avançados
- Padrões de projeto

### Testes (pytest)
- [Documentação pytest](https://docs.pytest.org)
- Fixtures e mocks
- Cobertura de testes

## ⚙️ Comandos Úteis

```bash
# Iniciar servidor
uvicorn app.main:app --reload

# Executar testes
pytest tests/ -v

# Ver documentação
http://localhost:8000/docs
```

## 📌 Arquivos Principais

### `main.py`
- Ponto de entrada
- Configuração FastAPI
- Middleware e CORS

### `crud_user.py`
- Operações de usuário
- Tratamento de erros
- Transações

### `models/user.py`
- Estrutura de tabelas
- Relacionamentos
- Tipos de dados

### `schemas/user.py`
- Validação
- Conversão de tipos
- Documentação

## 🎯 Próximos Passos

1. Estudar autenticação JWT
2. Aprofundar SQLAlchemy
3. Praticar testes
4. Otimização e cache

## 🔗 APIs Externas

### TMDB API
- Integração
- Endpoints principais
- Tratamento de erros

## 🔒 Segurança

- Autenticação JWT
- Proteção de rotas
- Validação de dados
- Tratamento de erros

## 📊 Banco de Dados

- SQLite em desenvolvimento
- Migrations
- Backups e recuperação
- Queries otimizadas