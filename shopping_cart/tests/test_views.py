from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

def create_product(pid, name, description, price, rating, copies_sold, on_sale, sale_price, image_url):
    return Product.objects.create(pid=pid, name=name, description=description, price=price, rating=rating, copies_sold=copies_sold, on_sale=on_sale, sale_price=sale_price, image_url=image_url)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.view_cart_url = reverse('view_cart')
        self.product1 = create_product(pid='1', name='product1', description='product1 description', price=1, rating=1, copies_sold=1, on_sale=True, sale_price=1, image_url='/image_url/')

    def test_view_cart(self):
        response = self.client.get(self.view_cart_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_cart/cart.html')
