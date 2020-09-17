from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product

def view_cart(request):

    context = {
        'on_cart_page': True
    }

    return render(request, 'shopping_cart/cart.html', context)

def add_item_to_cart(request, product_id):
    """ Add product to shopping cart """
    
    product = get_object_or_404(Product, pid=product_id)

    redirect_url = ''
    if request.POST:
        redirect_url = request.POST.get('redirect_url')

    if redirect_url == '':
        redirect_url = '/cart'

    cart = request.session.get('cart', {})
    if product_id in list(cart.keys()): 
        messages.warning(request,(f'{product.name} is already in cart'))
    else:
        cart[product_id] = 1
        messages.success(request,(f'{product.name} is added to cart'))

    request.session['cart'] = cart
    return redirect(redirect_url)

def remove_item_from_cart(request, product_id):
    try:
        product = get_object_or_404(Product, pid=product_id)
        
        redirect_url = ''
        if request.POST:
            redirect_url = request.POST.get('redirect_url')

        if redirect_url == '':
            redirect_url = reverse('view_cart')

        cart = request.session.get('cart', {})
        cart.pop(product_id)

        messages.success(request, f'Removed {product.name} from your cart.')

        request.session['cart'] = cart
        return redirect(redirect_url)
    except Exception as error:
        messages.error(request, f'Error removing: {error}')
        return redirect(redirect_url)
