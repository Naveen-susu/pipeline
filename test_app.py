import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):

        self.app = app.test_clinet()
        self.app.testing = Ture

    def test_welcome(self):

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.get_json(), {"message": "You are welcome!"})


if __name__ == '__main__':
    unittest.main()
