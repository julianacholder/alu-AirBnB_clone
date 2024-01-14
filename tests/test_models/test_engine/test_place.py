"""
doc
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    doc
    """
    def test_instance(self):
        """
        doc
        """
        inst = Place()
        self.assertTrue(hasattr(inst, "city_id"))
        self.assertTrue(hasattr(inst, "user_id"))
        self.assertTrue(hasattr(inst, "name"))
        self.assertTrue(hasattr(inst, "description"))
        self.assertTrue(hasattr(inst, "number_rooms"))
        self.assertTrue(hasattr(inst, "number_bathrooms"))
        self.assertTrue(hasattr(inst, "price_by_night"))
        self.assertTrue(hasattr(inst, "latitude"))
        self.assertTrue(hasattr(inst, "longitude"))
        self.assertTrue(hasattr(inst, "amenity_id"))

    def test_isBaseModelInstance(self):
        """
        doc
        """
        inst = Place()
        self.assertTrue(isinstance(inst, BaseModel))

    def test_attr(self):
        """
        doc
        """
        inst = Place()
        self.assertTrue(isinstance(inst.city_id, str))
        self.assertTrue(isinstance(inst.user_id, str))
        self.assertTrue(isinstance(inst.name, str))
        self.assertTrue(isinstance(inst.description, str))
        self.assertTrue(isinstance(inst.number_rooms, int))
        self.assertTrue(isinstance(inst.number_bathrooms, int))
        self.assertTrue(isinstance(inst.price_by_night, int))
        self.assertTrue(isinstance(inst.latitude, float))
        self.assertTrue(isinstance(inst.longitude, float))
        self.assertTrue(isinstance(inst.amenity_id, list))
        self.assertTrue(isinstance(inst.created_at, datetime))


if __name__ == '__main__':
    unittest.main()
