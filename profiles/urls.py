from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_id>', views.order_history),
    path('password/', views.change_password),
]
