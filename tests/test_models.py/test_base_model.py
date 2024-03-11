import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up an instance of BaseModel for testing."""
        self.base_model = BaseModel()


    def test_init(self):
        """Tests basic initialization of BaseModel.

        Tests that the id attribute is a string, created_at is a datetime,
        and updated_at is also a datetime, and that both are equal at
        initialization.
        """
        self.assertIsInstance(self.base_model.id, str, msg="id is not a string")
        self.assertIsInstance(self.base_model.created_at, datetime, msg="created_at is not a datetime")
        self.assertIsInstance(self.base_model.updated_at, datetime, msg="updated_at is not a datetime")
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at, msg="created_at and updated_at are not equal at init")

    def test_init_kwargs(self):
        """Tests initialization with valid keyword arguments."""
        custom_id = str(uuid.uuid4())
        custom_created_at = datetime.now() - timedelta(days=1)
        test_model = BaseModel(id=custom_id, created_at=custom_created_at.isoformat())
        self.assertEqual(test_model.id, custom_id)
        self.assertEqual(test_model.created_at, custom_created_at)

    def test_init_invalid_kwargs_type(self):
        """Tests initialization with invalid keyword argument types (non-string id, non-datetime created_at)."""
        with self.assertRaises(TypeError):
            BaseModel(id=123, created_at="invalid_format")  # Invalid id type
        with self.assertRaises(TypeError):
            BaseModel(id=str(uuid.uuid4()), created_at=123)  # Invalid created_at type

    def test_init_invalid_kwargs_format(self):
        """Tests initialization with invalid keyword argument format (invalid datetime format for created_at)."""
        with self.assertRaises(ValueError):
            BaseModel(id=str(uuid.uuid4()), created_at="invalid_format")

    def test_str(self):
        """Tests string representation of the instance."""
        expected_string = f"[ {self.base_model.__class__.__name__} ] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        """Tests update of updated_at on save."""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests conversion of the instance to a dictionary."""
        test_dict = self.base_model.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(test_dict["__class__"], self.base_model.__class__.__name__)
        self.assertEqual(test_dict["updated_at"], self.base_model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
