from rest_framework import status
from rest_framework.test import APITestCase
from api.models import AttributeName


class TestViews(APITestCase):
    def setUp(self):
        super().setUp()
        AttributeName.objects.create(id="1", name="Povrch")
        self.data = [{"AttributeName": {"id": 1, "name": "Barva"}}]
        self.attr_name_dict = self.data[0].get("AttributeName")

    def test_import_existing_model(self):
        """Test the status and import of valid data"""
        r = self.client.post("/import/", self.data, format="json")

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(
            AttributeName.objects.get(id=self.attr_name_dict.get("id")).name,
            self.attr_name_dict.get("name"),
        )

    def test_import_non_existent_model(self):
        """Test the status and import of invalid data"""
        data = [{"NonExistentModel": {"id": 1, "name": "Barva"}}]
        model_name = list(data[0].keys())[0]

        r = self.client.post("/import/", data, format="json").json()

        self.assertEqual(r["message"], f"{model_name} is not a valid model.")

    def test_get_model(self):
        """Test the model data validity on getModel view"""
        r = self.client.get("/detail/AttributeName/")

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(
            r.json()["message"],
            [
                {
                    "id": 1,
                    "name": "Povrch",
                    "code": None,
                    "display": False,
                }
            ],
        )

    def test_get_non_existent_model(self):
        """Test the model data validity on getModel view"""
        r = self.client.get("/detail/NonExistentModel/")

        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_entry(self):
        """Test the entry data validity on getEntry view"""
        r = self.client.get("/detail/AttributeName/1")

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(
            r.json()["message"],
            [
                {
                    "id": 1,
                    "name": "Povrch",
                    "code": None,
                    "display": False,
                }
            ],
        )

    def test_get_non_existent_entry(self):
        """Test the entry data validity on getEntry view"""
        r = self.client.get("/detail/AttributeName/2")

        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)
