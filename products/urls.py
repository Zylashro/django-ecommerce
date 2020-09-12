from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list_view, name='products_list'),
    path('<int:_id>/', views.products_detail_view, name='product_detail'),
    path('banner-products/', views.banner_products_view), 
    path('create/', views.products_create_view),
    path('<int:_id>/edit/', views.products_edit_view),
    path('<int:_id>/delete/', views.products_delete_view),
]
