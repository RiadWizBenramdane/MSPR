from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_delete_product():
    # test deleting an existing product
    response = client.delete("/products/50")
    assert response.status_code == 200

    # test deleting a non-existent product
    response = client.delete("/products/999")
    assert response.status_code == 404
    
    
def test_create_product():
     product = {
             "createdAt": "2023-02-19T13:42:19.010Z",
             "name": "Rex Bailey",
             "details": {
                "price": "659.00",
                "description": "The Nagasaki Lander is the trademarked name of several series of Nagasaki sport bikes, that started with the 1984 ABC800J",
                "color": "red"
            },
            "stock": 12059,    
    }   
     response = client.post("/products/",product)
     id_test = response.json()["id"]
     assert response.status_code == 200
     
     
# Test GET product by ID
def test_read_product():
     response = client.get("/products/"+str(id_test))
     
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
            "id": str(id_test)   
    }   
     response = client.get("/products/99999999999")
     assert response.status_code == 404

def test_update_product():
     response = client.get("/products/"+str(id_test))
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
            "id": str(id_test)    
    }   


