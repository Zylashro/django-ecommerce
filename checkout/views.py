from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

import stripe
import json

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
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
        return HttpResponse(content=error, status=400)

@login_required
def checkout(request, *args, **kwargs):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.shopping_cart = json.dumps(cart)
            order.save()
            for product_id, product_data in cart.items():
                try:
                    product = Product.objects.get(pid=product_id)
                    if isinstance(product_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your cart wasn't found.")
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                    'Please double check your information.'))
        
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'There is nothing in your cart at the moment.')
            return redirect(reverse('products_list'))
        
        current_cart = shopping_cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()


    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_id):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)

    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Order ID: {order_id}. A confirmation email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
