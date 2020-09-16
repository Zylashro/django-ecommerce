from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product
from checkout.models import Order
from profiles.models import UserProfile

import uuid

class License(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='licenses')
    key = models.CharField(max_length=254)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    date_acquired = models.DateTimeField(auto_now_add=True)

    def _generate_license_key(self):
        return uuid.uuid4().hex.upper()

    def save_key(self, *args, **kwargs):
        if not self.key:
            self.key = self._generate_license_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key
