from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe
import json

from .models import Order, OrderItem
from products.models import Product
from profiles.models import UserProfile
from shopping_cart.contexts import shopping_cart_contents

@require_POST
def cache_checkout(request, *args, **kwargs):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again.')
        return HttpResponse(status=400)

def checkout(request, *args, **kwargs):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        order = Order.object.get()
        cart = request.session.get('cart', {})
        pid = request.POST.get('client_secret').split('_secret')[0]
        order.stripe_pid = pid
        order.shopping_cart = json.dumps(cart)
        order.save()
        for product_id, product_data in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                if isinstance(product_data, int):
                    order_item = OrderItem(
                        order=order,
                        product=product,
                    )
                    order_item.save()
                else:
                    # Error message and redirect?
                    return HttpResponse(status=500)
            except Product.DoesNotExist:
                messages.error(request, "One of the products in your cart wasn't found.")
                order.delete()
                return redirect(reverse('view_cart'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'There is nothing in your cart at the moment.')
            return redirect(reverse('products'))
        
        current_cart = shopping_cart(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    context = {
        'order': order,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, context)

def checkout_success(request, order_id, *args, **kwargs):
    order = get_object_or_404(Order, order_id=order_id)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    messages.success(request, f'Order successfully processed! \
        Order ID: {order_id}. A confirmation email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, context)
