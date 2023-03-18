from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

# Test GET product by ID
def test_read_product():
     response = client.get("/products/1")
     assert response.status_code == 200
     assert response.json() == {
           "createdAt": "2023-02-19T13:42:19.010Z",
            "name": "Rex Bailey",
            "details": {
                "price": "659.00",
                "description": "The Nagasaki Lander is the trademarked name of several series of Nagasaki sport bikes, that started with the 1984 ABC800J",
                "color": "red"
            },
            "stock": 12059,
            "id": "1"    
    }   

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
