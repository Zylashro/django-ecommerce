from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

def create_product(pid, name, description, price, rating, copies_sold, on_sale, sale_price, image_url):
    return Product.objects.create(pid=pid, name=name, description=description, price=price, rating=rating, copies_sold=copies_sold, on_sale=on_sale, sale_price=sale_price, image_url=image_url)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.tac_url = reverse('tac')
        self.privacy_url = reverse('privacy')
        self.payment_url = reverse('payment')
        self.impressum_url = reverse('impressum')
        self.instructions_url = reverse('instructions')
        self.contact_url = reverse('contact')
        self.support_url = reverse('support')

    def test_index_get_sale_banner_products(self):
        banner_product1 = create_product(pid='1', name='product1', description='product1 description', price=1, rating=1, copies_sold=1, on_sale=True, sale_price=1, image_url='/image_url/')
        response = self.client.get(self.index_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_get_not_sale_banner_products(self):
        banner_product1 = create_product(pid='1', name='product1', description='product1 description', price=1, rating=1, copies_sold=1, on_sale=False, sale_price=0, image_url='/image_url/')
        response = self.client.get(self.index_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_tac_template_used(self):
        response = self.client.get(self.tac_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/tac.html')

    def test_privacy_template_used(self):
        response = self.client.get(self.privacy_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy.html')

    def test_payment_template_used(self):
        response = self.client.get(self.payment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/payment.html')

    def test_impressum_template_used(self):
        response = self.client.get(self.impressum_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/impressum.html')

    def test_instructions_template_used(self):
        response = self.client.get(self.instructions_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/instructions.html')

    def test_contact_template_used(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_support_template_used(self):
        response = self.client.get(self.support_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/support.html')
