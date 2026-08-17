import uuid

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# test the api 

def test_root():
    response = client.get("/")
    # expect response 
    assert response.status_code ==200
    assert response.json()== {"message": "API is running"}


def test_register():
    response = client.post("/register", json={
        "name": "natwar",
        "email": f"natwar-{uuid.uuid4().hex}@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}