"""
doc
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    doc
    """
    def test_user_attr(self):
        inst = User()
        self.assertTrue(hasattr(inst, "email"))
        self.assertTrue(hasattr(inst, "password"))
        self.assertTrue(hasattr(inst, "last_name"))
        self.assertTrue(hasattr(inst, "first_name"))

    def test_attr_type(self):
        """
        doc
        """
        inst = User()
        self.assertTrue(isinstance(inst.email, str))
        self.assertTrue(isinstance(inst.password, str))
        self.assertTrue(isinstance(inst.last_name, str))
        self.assertTrue(isinstance(inst.first_name, str))

    def test_isInstance(self):
        """
        doc
        """
        inst = User()
        self.assertTrue(isinstance(inst, BaseModel))


if __name__ == '__main__':
    unittest.main()
