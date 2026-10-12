#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_is_subclass(self):
        """Tests that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """Tests that a City instance is created correctly."""
        c = City()
        self.assertIsInstance(c, City)

    def test_attributes_exist(self):
        """Tests that City has required attributes."""
        c = City()
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(hasattr(c, 'state_id'))


if __name__ == '__main__':
    unittest.main()
