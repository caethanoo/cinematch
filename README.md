#  CineMatch: Um Projeto de Estudo Full-Stack

 ## 🚀 Sobre o Projeto

O **CineMatch** é uma aplicação web full-stack desenvolvida como parte de uma jornada de estudos e aprofundamento em tecnologias modernas de desenvolvimento web. A proposta da aplicação é ser um "Tinder para filmes", onde usuários podem dar "swipe" em filmes e descobrir quais deles seus amigos também gostaram, gerando "matches" de filmes em comum.

Este repositório serve como um diário de bordo do meu aprendizado, documentando o processo de construção de uma aplicação do zero, seguindo as melhores práticas de mercado em arquitetura, segurança e desenvolvimento.

## 🎯 Objetivo do Estudo

O principal objetivo deste projeto é adquirir experiência prática e demonstrável nas seguintes áreas:

* **Desenvolvimento Backend:** Construção de uma API RESTful robusta, segura e escalável.
* **Desenvolvimento Frontend:** Criação de uma interface de usuário moderna, responsiva e interativa.
* **Arquitetura de Software:** Aplicação de padrões de projeto para criar um código limpo, organizado e de fácil manutenção.
* **Boas Práticas:** Utilização de ferramentas como controle de versão (Git), testes automatizados e integração contínua.

## 🏛️ Arquitetura do Backend

O backend deste projeto foi estruturado seguindo um padrão de **Arquitetura em Camadas (Layered Architecture)**, inspirado em práticas recomendadas pela comunidade FastAPI. Esta abordagem visa a **Separação de Responsabilidades (Separation of Concerns)**, dividindo a aplicação em partes lógicas e independentes.

## 🛠️ Tecnologias Utilizadas

### Backend
* **Linguagem:** Python 3.11+
* **Framework:** FastAPI
* **Banco de Dados:** PostgreSQL com SQLAlchemy (ORM) e Alembic (Migrações)
* **Validação de Dados:** Pydantic
* **Autenticação:** JWT (JSON Web Tokens) e Passlib (Hashing de Senhas)
* **Servidor:** Uvicorn

### Frontend (Planejado)
* **Framework:** Next.js (React)
* **Estilização:** Tailwind CSS
* **Gerenciamento de Estado:** React Context API / Zustand
* **Consumo de API:** Axios / Fetch API


## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento do backend.

**Pré-requisitos:**
* Python 3.10+
* Git

**Passo a Passo:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/cinematch-fullstack.git](https://github.com/seu-usuario/cinematch-fullstack.git)
    ```

2.  **Navegue para a pasta do backend:**
    ```bash
    cd cinematch-fullstack/backend
    ```

3.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Linux/Mac
    source venv/bin/activate

    # Ativar no Windows
    .\venv\Scripts\activate
    ```

4.  **Configure as variáveis de ambiente:**
    * Copie o ficheiro de exemplo `.env.example` para um novo ficheiro chamado `.env`.
        ```bash
        # No Linux/Mac
        cp .env.example .env

        # No Windows
        copy .env.example .env
        ```
    * Abra o ficheiro `.env` e preencha os valores das variáveis, especialmente a sua `SECRET_KEY` e a `TMDB_API_KEY`.

5.  **Instale as dependências do projeto:**
    * O comando abaixo irá ler o ficheiro `pyproject.toml` e instalar todas as bibliotecas necessárias (FastAPI, SQLAlchemy, etc.).
    ```bash
    pip install -e .
    ```

## ▶️ Como Executar

Com o ambiente configurado, basta ligar o servidor de desenvolvimento.

1.  **Ligue o servidor Uvicorn:**
    * Certifique-se de que está na pasta `backend` e que o seu ambiente virtual (`venv`) está ativo.
    ```bash
    python -m uvicorn app.main:app --reload
    ```

2.  **Aceda à aplicação:**
    * O servidor estará a correr em `http://127.0.0.1:8000`.
    * A documentação interativa da API (Swagger UI) estará disponível em: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**.

##  Roadmap do Projeto

- [ ] Estrutura inicial do projeto e setup do ambiente
- [ ] **Semana 1:** Sistema de autenticação de usuários (Cadastro e Login)
- [ ] **Semana 2:** Lógica principal (Filmes, Swipes, Matches) e integração com a API do TMDB
- [ ] **Semana 3-4:** Desenvolvimento da interface do usuário com Next.js
- [ ] **Semana 5:** Testes, Dockerização e Deploy

---

Este projeto está sendo desenvolvido sob a orientação de um mentor técnico, com foco no aprendizado detalhado e na compreensão dos "porquês" por trás de cada decisão de código e arquitetura.

Autora: Brennda Caitano , bcaethano21@gmail.com, Linkedin: Brennda Caitano , Github: Caethannoo