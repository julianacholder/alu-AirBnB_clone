import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def test_attr(self):
        """
        doc
        """
        inst = City()
        self.assertTrue(hasattr(inst, "name"))
        self.assertTrue(hasattr(inst, "state_id"))

    def test_attr_type(self):
        """
        doc
        """
        inst = City()
        self.assertTrue(isinstance(inst.name, str))
        self.assertTrue(isinstance(inst.state_id, str))

    def test_isInstance(self):
        """
        doc
        """
        inst = City()
        self.assertTrue(isinstance(inst, BaseModel))


if __name__ == '__main__':
    unittest.main()
