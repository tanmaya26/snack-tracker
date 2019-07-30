from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Snacks
from .serializers import SnacksSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_snack(snack_name="", snack_quantity="", snack_description=""):
        if snack_name != "" and snack_quantity != "":
            Snacks.objects.create(snack_name=snack_name, snack_quantity=snack_quantity,
                                  snack_description=snack_description)

    def setUp(self):
        self.create_snack("Protein bar", 2, "Cliff bar")
        self.create_snack("Potato chips", 4, "Lays")


class GetAllSnacksTest(BaseViewTest):

    def test_get_all_snacks(self):
        response = self.client.get(
            reverse("snacks-all", kwargs={"version": "v1"})
        )

        expected = Snacks.objects.all()
        serialized = SnacksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
