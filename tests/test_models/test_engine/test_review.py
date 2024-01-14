"""
doc
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attr(self):
        """
        doc
        """
        inst = Review()
        self.assertTrue(hasattr(inst, "place_id"))
        self.assertTrue(hasattr(inst, "user_id"))
        self.assertTrue(hasattr(inst, "text"))

    def test_attr_type(self):
        inst = Review()
        self.assertTrue(isinstance(inst.text, str))
        self.assertTrue(isinstance(inst.place_id, str))
        self.assertTrue(isinstance(inst.user_id, str))

    def test_isInstance(self):
        inst = Review()
        self.assertTrue(isinstance(inst, BaseModel))


if __name__ == '__main__':
    unittest.main()
