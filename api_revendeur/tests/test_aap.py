from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

test_id=0
# Test POST customer
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
    
# Test GET customer by ID
# def test_read_customer():
#     response = client.get("/customers/1")
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": test_id,
#         "name": "Jane Doe",
#         "email": "john.smith@example.com",
#         "phone": "+1 123 456 7890",
#         "address": "123 Main St, Anytown USA"
#     }

# # Test GET non-existent customer by ID
# def test_read_nonexistent_customer():
#     response = client.get("/customers/99")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Customer not found"}


# # Test PUT customer by ID
# def test_update_customer():
#     updated_customer = {
#         "name": "Jhon Doe",
#     }
#     response = client.put("/customers/"+str(test_id), json=updated_customer)
#     assert response.status_code == 200
#     assert response.json() == {"id": test_id}

# # Test DELETE customer by ID
# def test_delete_customer():
#     response = client.delete("/customers/1")
#     assert response.status_code == 200
#     assert response.json() == {"id": 1}
