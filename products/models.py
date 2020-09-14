from django.db import models
from django.core.validators import MaxValueValidator

class Product(models.Model):
    _id = models.CharField(max_length=254, primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=1, decimal_places=2, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    copies_sold = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def discount(self):
        if self.on_sale:
            discount_amount = 75
            calculate_discount = (self.price / 100) * discount_amount
            calculate_price = self.price - calculate_discount
            self.price = calculate_price
            self.save()
