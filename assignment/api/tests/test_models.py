from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from api.models import AttributeName
import random, string


class TestModels(APITestCase):
    def test_attribute_name_max_len(self):
        """Test the max length of the AttributeName's name attribute"""
        invalid_string = "".join(
            random.choice(string.ascii_letters) for _ in range(256)
        )
        valid_string = "".join(random.choice(string.ascii_letters) for _ in range(255))

        AttributeName(name=invalid_string, display=False)
        self.assertRaises(ValidationError)

        AttributeName(name=valid_string, display=False, code=invalid_string)
        self.assertRaises(ValidationError)

    def test_attribute_name_blank_name(self):
        """Test the requirement of the AttributeName's name attribute"""
        AttributeName(display=False)
        self.assertRaises(ValidationError)

    # ...
