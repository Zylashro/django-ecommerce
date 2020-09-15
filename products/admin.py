from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = (
        'pid',
        'name',
        'price',
        'rating',
        'date_added',
        'copies_sold',
        'on_sale',
        'sale_price',
        'image',
    )

    ordering = ('date_added',)

admin.site.register(Product, ProductAdmin)
