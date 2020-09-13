from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product

def view_cart(request, *args, **kwargs):
    return render(request, 'cart/cart.html')

def add_item_to_cart(request, product_id, *args, **kwargs):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect')
    request.session['cart'] = cart
    return redirect(redirect_url)

def remove_item_from_cart(request, product_id, *args, **kwargs):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        cart.pop(product_id)
        messages.success(request, f'Removed {product.name} from your cart.')
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, f'Error removing: {error}')
        return HttpResponse(status=500)
