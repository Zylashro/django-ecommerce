from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_id>/', views.order_history),
    path('licenses_owned/<id>/', views.licenses_owned),
    path('password/', views.change_password, name=change_password),
]
