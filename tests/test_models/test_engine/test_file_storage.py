#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
from unittest import skipIf
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')


@skipIf(STORAGE_TYPE == 'db', "Skipping FileStorage tests for db storage")
class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Sets up a fresh FileStorage instance for each test."""
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        """Tests that all() returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_with_class_filter(self):
        """Tests that all(cls) filters by class."""
        obj = State()
        obj.name = "TestState"
        self.storage.new(obj)
        result = self.storage.all(State)
        for key in result:
            self.assertIn('State', key)

    def test_new_adds_object(self):
        """Tests that new() adds an object to storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage.all())

    def test_delete_removes_object(self):
        """Tests that delete() removes an object from storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage.all())
        self.storage.delete(obj)
        self.assertNotIn(key, self.storage.all())

    def test_delete_none_does_nothing(self):
        """Tests that delete(None) does not raise an error."""
        try:
            self.storage.delete(None)
        except Exception as e:
            self.fail("delete(None) raised {}".format(e))

    def test_save_and_reload(self):
        """Tests that save() and reload() persist objects."""
        obj = State()
        obj.name = "Persist"
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "State.{}".format(obj.id)
        self.assertIn(key, new_storage.all())


@skipIf(STORAGE_TYPE != 'db', "Skipping DBStorage tests for file storage")
class TestFileStorageSkipped(unittest.TestCase):
    """Placeholder tests when using db storage."""

    def test_db_storage_active(self):
        """Tests that db storage is active when HBNB_TYPE_STORAGE=db."""
        self.assertEqual(STORAGE_TYPE, 'db')


if __name__ == '__main__':
    unittest.main()
