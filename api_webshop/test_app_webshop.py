import unittest
from fastapi.testclient import TestClient
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_protected_endpoint_without_token_should_fail(self):
        response = self.client.get("/protected")
        self.assertEqual(response.status_code, 401)

    def test_protected_endpoint_with_invalid_token_should_fail(self):
        response = self.client.get("/protected", headers={"Authorization": "Bearer invalid_token"})
        self.assertEqual(response.status_code, 401)

    def test_protected_endpoint_with_valid_token_should_succeed(self):
        access_token = self._get_access_token()
        response = self.client.get("/protected", headers={"Authorization": f"Bearer {access_token}"})
        self.assertEqual(response.status_code, 200)

    def test_send_qr_code_endpoint_should_succeed(self):
        access_token = self._get_access_token()
        response = self.client.get("/send_qr_code/user1@example.com", headers={"Authorization": f"Bearer {access_token}"})
        self.assertEqual(response.status_code, 200)

    def _get_access_token(self):
        response = self.client.post("/auth", json={"username": "admin", "password": "admin"})
        return response.json()["access_token"]

if __name__ == '__main__':
    unittest.main()
