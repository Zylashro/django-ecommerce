from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def save_order_item_total(sender, instance, created, **kwargs):
    instance.order.update_total()

@receiver(post_delete, sender=OrderItem)
def delete_order_item_total(sender, instance, **kwargs):
    instance.order.update_total()
