#!/usr/bin/python3
"""
testing BaseModel
"""
from unittest import mock
from models.base_model import BaseModel
from models import storage
import models
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """
    testBaseModel
    """
    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """
        testing the save method
        """
        Bm = BaseModel()
        first_updated = Bm.updated_at
        Bm.save()
        self.assertNotEqual(first_updated, Bm.updated_at)

    def test_to_dict(self):
        """
        testing to_dict()
        """
        Bm = BaseModel()
        self.assertIsInstance(Bm.to_dict(), dict)
        self.assertTrue(all([key in Bm.to_dict() for key in Bm.__dict__]))
        self.assertTrue("__class__" in Bm.to_dict())

    def test_id(self):
        """
        testing if id is of type str
        """
        Bm = BaseModel()
        self.assertIsInstance(Bm.id, str)

    def test_created_at(self):
        """
        testing created_at
        """
        Bm = BaseModel()
        self.assertIsInstance(Bm.created_at, datetime)
        self.assertEqual(Bm.created_at, Bm.updated_at)

    def test_str(self):
        """
        testing str
        """
        Bm = BaseModel()
        string = f"[{Bm.__class__.__name__}] ({Bm.id}) {Bm.__dict__}"
        self.assertEqual(string, str(Bm))


if __name__ == '__main__':
    unittest.main()
