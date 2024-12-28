import unittest
from app.routes import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Authorization": "securetoken123"}

    def test_add_book(self):
        response = self.client.post(
            "/books",
            json={"title": "Book 1", "author": "Author 1"},
            headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Book added", response.json["message"])

    def test_list_books(self):
        self.client.post(
            "/books",
            json={"title": "Book 1", "author": "Author 1"},
            headers=self.headers
        )
        response = self.client.get("/books?page=1&per_page=5", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["books"]), 1)

    def test_unauthorized_access(self):
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 401)

    def test_delete_book(self):
        self.client.post(
            "/books",
            json={"title": "Book 1", "author": "Author 1"},
            headers=self.headers
        )
        response = self.client.delete("/books/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Book deleted", response.json["message"])

if __name__ == "__main__":
    unittest.main()
