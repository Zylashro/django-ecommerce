from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shopping_cart.views import view_cart, add_item_to_cart, remove_item_from_cart

class TestUrls(SimpleTestCase):

    def test_view_cart_is_resolved(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_item_to_cart_is_resolved(self):
        url = reverse('add_to_cart', args=['1'])
        self.assertEquals(resolve(url).func, add_item_to_cart)

    def test_remove_item_from_cart_is_resolved(self):
        url = reverse('remove_from_cart', args=['1'])
        self.assertEquals(resolve(url).func, remove_item_from_cart)
