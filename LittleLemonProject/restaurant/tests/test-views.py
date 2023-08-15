from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item = Menu.objects.create(title="Burger", price=10.50, inventory=50)

    def test_get_menu_list(self):
        response = self.client.get(reverse("menu-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Burger", count=1)

    def test_get_single_menu_item(self):
        response = self.client.get(reverse("menu-single", args=[self.menu_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Burger")
