from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile

class TestUrls(SimpleTestCase):

    def test_profile_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)
