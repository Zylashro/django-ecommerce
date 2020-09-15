from django.db import models

class Product(models.Model):
    pid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    copies_sold = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
