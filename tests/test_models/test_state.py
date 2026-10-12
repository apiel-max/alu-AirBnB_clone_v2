#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_is_subclass(self):
        """Tests that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """Tests that a State instance is created correctly."""
        s = State()
        self.assertIsInstance(s, State)

    def test_name_attribute(self):
        """Tests that State has a name attribute."""
        s = State()
        self.assertTrue(hasattr(s, 'name'))


if __name__ == '__main__':
    unittest.main()
