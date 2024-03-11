#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up an instance of BaseModel for testing."""
        self.base_model = BaseModel()

    def test_str(self):
        """Tests string representation of the instance."""
        expected_string = f"[ {self.base_model.__class__.__name__} ]({self.base_model.id}) {self.base_model.__dict__}"
        print(f"what it is returning:{str(self.base_model)}\n")
        print(f"expected outcome: {expected_string}\n")
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        """Tests update of updated_at on save."""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, 
			initial_updated_at)

    def test_to_dict(self):
        """Tests conversion of the instance to a dictionary."""
        test_dict = self.base_model.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["created_at"],
			self.base_model.created_at.isoformat())
        self.assertEqual(test_dict["__class__"],
			self.base_model.__class__.__name__)
        self.assertEqual(test_dict["updated_at"],
			self.base_model.updated_at.isoformat())



if __name__ == "__main__":
    unittest.main()
