from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart),
    path('add/<product_id>', views.add_item_to_cart),
    path('remove/<product_id>', views.remove_item_from_cart),
]
