from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('profiles.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('checkout/', include('checkout.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
