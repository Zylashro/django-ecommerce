from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, tac, privacy, payment, impressum, instructions, contact, support

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_tac_url_is_resolved(self):
        url = reverse('tac')
        self.assertEquals(resolve(url).func, tac)

    def test_privacy_url_is_resolved(self):
        url = reverse('privacy')
        self.assertEquals(resolve(url).func, privacy)

    def test_payment_url_is_resolved(self):
        url = reverse('payment')
        self.assertEquals(resolve(url).func, payment)

    def test_impressum_url_is_resolved(self):
        url = reverse('impressum')
        self.assertEquals(resolve(url).func, impressum)

    def test_instructions_url_is_resolved(self):
        url = reverse('instructions')
        self.assertEquals(resolve(url).func, instructions)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_support_url_is_resolved(self):
        url = reverse('support')
        self.assertEquals(resolve(url).func, support)
