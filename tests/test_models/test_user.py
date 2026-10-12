#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_is_subclass(self):
        """Tests that User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """Tests that a User instance is created correctly."""
        u = User()
        self.assertIsInstance(u, User)

    def test_attributes_exist(self):
        """Tests that User has required class attributes."""
        u = User()
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))


if __name__ == '__main__':
    unittest.main()
