from django.db import models
from django.db.models import Sum

from products.models import Product
from profiles.models import UserProfile

import uuid

class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False, primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    shopping_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_id(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total = self.items.aggregate(Sum('item_total'))['item_total__sum'] or 0
        self.save()

    def save_order(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=Flase)

    def save_order_item(self, *args, **kwargs):
        self.item_total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product._id} on order {self.order.order_id}'
