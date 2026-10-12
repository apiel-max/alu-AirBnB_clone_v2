#!/usr/bin/python3
"""Unit tests for the DBStorage class."""
import unittest
import os
from unittest import skipIf

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')


@skipIf(STORAGE_TYPE != 'db', "Skipping DBStorage tests for file storage")
class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class."""

    def setUp(self):
        """Sets up storage for each test."""
        import models
        self.storage = models.storage

    def test_all_returns_dict(self):
        """Tests that all() returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_with_class_filter(self):
        """Tests that all(cls) filters by class."""
        from models.state import State
        result = self.storage.all(State)
        for key in result:
            self.assertIn('State', key)

    def test_new_and_save(self):
        """Tests that new() and save() persist an object."""
        from models.state import State
        import MySQLdb
        conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM states")
        count_before = cur.fetchone()[0]
        cur.close()
        conn.close()

        state = State(name="TestState")
        self.storage.new(state)
        self.storage.save()

        conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM states")
        count_after = cur.fetchone()[0]
        cur.close()
        conn.close()

        self.assertEqual(count_after, count_before + 1)
        self.storage.delete(state)
        self.storage.save()

    def test_delete(self):
        """Tests that delete() removes an object from the database."""
        from models.state import State
        state = State(name="DeleteMe")
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        self.storage.save()
        key = "State.{}".format(state.id)
        self.assertNotIn(key, self.storage.all(State))


@skipIf(STORAGE_TYPE == 'db', "Skipping file storage placeholder for db mode")
class TestDBStorageSkipped(unittest.TestCase):
    """Placeholder tests when using file storage."""

    def test_file_storage_active(self):
        """Tests that file storage is active when HBNB_TYPE_STORAGE != db."""
        self.assertNotEqual(STORAGE_TYPE, 'db')


if __name__ == '__main__':
    unittest.main()
