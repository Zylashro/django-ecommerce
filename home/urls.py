from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tac/', views.tac, name='tac'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment/', views.payment, name='payment'),
    path('impressum/', views.impressum, name='impressum'),
    path('instructions/', views.instructions, name='instructions'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
]