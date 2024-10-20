from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
   def test_add_item(self):
      item = Menu.objects.create(title = 'NewItemTest', price = 1.00, inventory = 1)
      self.assertEqual(item.__str__(), "NewItemTest : 1.0")
