#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_creation(self):
        """Tests that a BaseModel instance is created correctly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_ids(self):
        """Tests that two instances have different ids."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_representation(self):
        """Tests the string representation of a BaseModel instance."""
        obj = BaseModel()
        s = str(obj)
        self.assertIn('BaseModel', s)
        self.assertIn(obj.id, s)

    def test_to_dict(self):
        """Tests that to_dict returns a proper dictionary."""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)
        self.assertNotIn('_sa_instance_state', d)

    def test_kwargs_init(self):
        """Tests initialization from a dictionary."""
        obj = BaseModel()
        d = obj.to_dict()
        obj2 = BaseModel(**d)
        self.assertEqual(obj.id, obj2.id)
        self.assertIsInstance(obj2.created_at, datetime)

    def test_save_updates_updated_at(self):
        """Tests that save() updates the updated_at attribute."""
        obj = BaseModel()
        old_updated = obj.updated_at
        obj.save()
        self.assertGreaterEqual(obj.updated_at, old_updated)


if __name__ == '__main__':
    unittest.main()
