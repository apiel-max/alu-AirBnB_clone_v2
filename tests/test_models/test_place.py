#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_is_subclass(self):
        """Tests that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """Tests that a Place instance is created correctly."""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_attributes_exist(self):
        """Tests that Place has required attributes."""
        p = Place()
        for attr in ['city_id', 'user_id', 'name', 'description',
                     'number_rooms', 'number_bathrooms', 'max_guest',
                     'price_by_night', 'latitude', 'longitude']:
            self.assertTrue(hasattr(p, attr))


if __name__ == '__main__':
    unittest.main()
