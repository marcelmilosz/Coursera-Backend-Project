from django.test import TestCase
from ..models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        expected_representation = "IceCream : 80"
        self.assertEqual(str(item), expected_representation)
