"""
doc
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    doc
    """
    def test_attr(self):
        """
        doc
        """
        inst = State()
        self.assertTrue(hasattr(inst, "name"))

    def test_attr_type(self):
        """
        doc
        """
        inst = State()
        self.assertTrue(isinstance(inst.name, str))

    def test_isInstance(self):
        """
        doc
        """
        inst = State()
        self.assertTrue(isinstance(inst, BaseModel))


if __name__ == '__main__':
    unittest.main()
