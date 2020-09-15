from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product
from checkout.models import Order

@receiver(post_save, sender=Order)
def update_copies_sold(sender, instance, **kwargs):
    copies_sold_add = Product.copies_sold + 1
    instance.Product.save(copies_sold_add)
