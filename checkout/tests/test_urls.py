from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout, checkout_success, cache_checkout
from checkout.webhooks import webhook

class TestUrls(SimpleTestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_success_url_is_resolved(self):
        url = reverse('checkout_success', args=['1'])
        self.assertEquals(resolve(url).func, checkout_success)

    def test_cache_checkout_is_resolved(self):
        url = reverse('cache_checkout_data')
        self.assertEquals(resolve(url).func, cache_checkout)

    def test_webhook_is_resolved(self):
        url = reverse('webhook')
        self.assertEquals(resolve(url).func, webhook)
