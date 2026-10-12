#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_is_subclass(self):
        """Tests that Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """Tests that a Review instance is created correctly."""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_attributes_exist(self):
        """Tests that Review has required attributes."""
        r = Review()
        self.assertTrue(hasattr(r, 'text'))
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))


if __name__ == '__main__':
    unittest.main()
