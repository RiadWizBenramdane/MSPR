from fastapi.testclient import TestClient
from app import app
from typing import List
import requests

client = TestClient(app)


def test_create_products():
    new_products = {
        "name": "Jane Doe",
        "stock": "10253",
        "id": "5000",
    }
    response = client.post("/customers/", json=new_products)  
    assert (response.status_code == 200) or (response.status_code == 201)
    assert response.json().name == "Jane Doe"
    assert response.json().stock == "10253"
