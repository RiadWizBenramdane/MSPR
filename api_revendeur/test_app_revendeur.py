import json
import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

# Test GET /products/{product_id}
def test_read_product():
    # Make a request to the endpoint with product_id=1
    response = client.get("/products/1")
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response contains a "name" field
    assert "name" in response.json()

# Test POST /products/
def test_create_product():
    # Define the data to send in the request
    product_data = {"name": "Test Product", "description": "This is a test product."}
    # Make a request to the endpoint with the product data
    response = client.post("/products/", json=product_data)
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response contains an "id" field
    assert "id" in response.json()

# Test PUT /products/{product_id}
def test_update_product():
    # Define the data to send in the request
    product_data = {"name": "Updated Product Name", "description": "This product has been updated."}
    # Make a request to the endpoint with product_id=1 and the updated data
    response = client.put("/products/1", json=product_data)
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response contains an "id" field
    assert "id" in response.json()

# Test DELETE /products/{product_id}
def test_delete_product():
    # Make a request to the endpoint with product_id=1
    response = client.delete("/products/1")
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response contains an "id" field
    assert "id" in response.json()
