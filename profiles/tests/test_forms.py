from django.test import SimpleTestCase
from profiles.forms import UserProfileForm

class TestForms(SimpleTestCase):

    def test_user_profile_form_valid_data(self):
        form = UserProfileForm(data={
            'Phone Number': 123456789,
            'Postal Code': 38,
            'Town or City': 'Test Town',
            'Street Address 1': 'Test street 1',
            'Street Address 2': 'Test street 2',
            'County, State or Locality': 'Test county',
        })

        self.assertTrue(form.is_valid())
