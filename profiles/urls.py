from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    # path('login/', views.profile_login, name='profile_login'),
]
