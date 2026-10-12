#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_is_subclass(self):
        """Tests that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """Tests that an Amenity instance is created correctly."""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_name_attribute(self):
        """Tests that Amenity has a name attribute."""
        a = Amenity()
        self.assertTrue(hasattr(a, 'name'))


if __name__ == '__main__':
    unittest.main()
