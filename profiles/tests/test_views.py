from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')

    def test_profile(self):
        response = self.client.get(self.profile_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')     
