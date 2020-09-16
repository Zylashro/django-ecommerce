from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import products_list_view, products_detail_view

class TestUrls(SimpleTestCase):

    def test_products_list_view_url_is_resolved(self):
        url = reverse('products_list')
        self.assertEquals(resolve(url).func, products_list_view)

    def test_products_detail_view_url_is_resolved(self):
        url = reverse('product_detail', args=['1'])
        self.assertEquals(resolve(url).func, products_detail_view)
