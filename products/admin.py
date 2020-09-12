from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = (
        '_id',
        'name',
        'price',
        'rating',
        'date_added',
        'copies_sold',
        'on_sale',
        'image',
    )

    ordering = ('date_added',)

admin.site.register(Product, ProductAdmin)
