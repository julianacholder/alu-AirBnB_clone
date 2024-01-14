"""
test amenity
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenity(unittest.TestCase):
    """
    test Amenity
    """
    def test_isInstance(self):
        """
        test if it is an instance of BaseModel
        """
        inst = Amenity()
        self.assertTrue(isinstance(inst, BaseModel))

    def test_attr(self):
        """
        testing the attr
        """
        inst = Amenity()
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))
        self.assertTrue(hasattr(inst, "name"))

    def test_name(self):
        """
        testing the name attr
        """
        inst = Amenity()
        self.assertTrue(type(inst.name), str)
        self.assertTrue(isinstance(inst.created_at, datetime))
        self.assertTrue(isinstance(inst.id, str))


if __name__ == '__main__':
    unittest.main()
