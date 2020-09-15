from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout),
    path('checkout_success/<order_id>', views.checkout_success),
    path('cache_checkout_data/', views.cache_checkout),
    path('wh/', webhook),
]
