from django.db import models
from django.core.validators import MaxValueValidator

class Product(models.Model):
    pid = models.CharField(max_length=254, primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
<<<<<<< HEAD
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
=======
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
>>>>>>> products
    date_added = models.DateField(auto_now_add=True)
    copies_sold = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
