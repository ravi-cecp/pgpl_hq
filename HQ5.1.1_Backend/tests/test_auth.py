# UTC Timestamp: <insert UTC timestamp here>
# File: tests/test_auth.py

import unittest
from werkzeug.security import check_password_hash
from services.auth_service import create_user_service, validate_user_service
from configs.db import db

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass"
        self.role = "Admin"

    def tearDown(self):
        db.users.delete_many({"username": self.username})

    def test_create_user(self):
        create_user_service(self.username, self.password, self.role)
        user = db.users.find_one({"username": self.username})
        self.assertIsNotNone(user)
        self.assertTrue(check_password_hash(user['password'], self.password))

    def test_validate_user(self):
        create_user_service(self.username, self.password, self.role)
        user = validate_user_service(self.username, self.password)
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
