#!/usr/bin/python3
"""Unit tests for the console's do_create with key=value parameters."""
import unittest
import os
from unittest import skipIf
from unittest.mock import patch
from io import StringIO
from console import HBnBCommand
import models

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')


@skipIf(STORAGE_TYPE == 'db', "Console param tests only for FileStorage")
class TestConsoleCreate(unittest.TestCase):
    """Test cases for the do_create command with parameters."""

    def tearDown(self):
        """Cleans up file.json after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_create_no_class(self):
        """Tests create with no class name prints error."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd('create')
        self.assertIn('class name missing', f.getvalue())

    def test_create_invalid_class(self):
        """Tests create with invalid class name prints error."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd('create MyModel')
        self.assertIn("class doesn't exist", f.getvalue())

    def test_create_state_with_name(self):
        """Tests create State with name parameter."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd('create State name="California"')
        obj_id = f.getvalue().strip()
        self.assertTrue(len(obj_id) > 0)
        key = "State.{}".format(obj_id)
        self.assertIn(key, models.storage.all())
        self.assertEqual(models.storage.all()[key].name, 'California')

    def test_create_with_underscore_in_string(self):
        """Tests that underscores in string values are replaced by spaces."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd('create State name="My_little_state"')
        obj_id = f.getvalue().strip()
        key = "State.{}".format(obj_id)
        self.assertEqual(models.storage.all()[key].name, 'My little state')

    def test_create_with_integer_param(self):
        """Tests create with an integer parameter."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd(
                'create Place name="Test" number_rooms=3 city_id="abc" '
                'user_id="xyz"')
        obj_id = f.getvalue().strip()
        key = "Place.{}".format(obj_id)
        self.assertEqual(models.storage.all()[key].number_rooms, 3)

    def test_create_with_float_param(self):
        """Tests create with a float parameter."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd(
                'create Place name="Test" latitude=37.77 city_id="abc" '
                'user_id="xyz"')
        obj_id = f.getvalue().strip()
        key = "Place.{}".format(obj_id)
        self.assertAlmostEqual(models.storage.all()[key].latitude, 37.77)

    def test_create_skips_invalid_params(self):
        """Tests that invalid parameters are skipped."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBnBCommand().onecmd('create State name="Valid" bad_param')
        obj_id = f.getvalue().strip()
        key = "State.{}".format(obj_id)
        obj = models.storage.all()[key]
        self.assertEqual(obj.name, 'Valid')
        self.assertFalse(hasattr(obj, 'bad_param'))


if __name__ == '__main__':
    unittest.main()
