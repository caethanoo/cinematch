import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.api.deps import get_db

# Configuração do banco de teste
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {
        "email": "test@example.com",
        "password": "test123",
        "name": "Test User"
    }
    response = client.post("/users/", json=user_data)
    return response.json()

@pytest.fixture
def auth_headers(client, test_user):
    login_data = {
        "username": test_user["email"],
        "password": "test123"
    }
    response = client.post("/users/token", data=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

# Testes de Usuário
def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "test123", "name": "Test User"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"

def test_login_user(client, test_user):
    response = client.post(
        "/users/token",
        data={"username": test_user["email"], "password": "test123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

# Testes de Filmes
def test_get_next_movies(client, auth_headers):
    response = client.get("/movies/next", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_movie_details(client, auth_headers):
    movie_id = 550  # Fight Club
    response = client.get(f"/movies/{movie_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == movie_id

# Testes de Swipes
def test_create_swipe(client, auth_headers):
    swipe_data = {
        "movie_id": 550,
        "liked": True
    }
    response = client.post("/swipes/", json=swipe_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["movie_id"] == 550
    assert data["liked"] == True

def test_get_user_swipes(client, auth_headers):
    response = client.get("/swipes/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)