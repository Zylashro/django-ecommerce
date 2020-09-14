from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import License
from checkout.models import Order

@receiver(post_save, sender=Order)
def create_license(sender, instance, created, **kwargs):
    if created:
        License.objects.create(instace=Order)

    instance.License.save()
