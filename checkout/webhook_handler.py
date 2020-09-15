from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class Stripe_Webhook_Handler:
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        return HttpResponse(status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart

        billing_details = intent.charges.data[0].billing_details
        total = round(intent.charges.data[0].amount / 100, 2)

        profile = None
        username = intent.metadata.username

        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    email__iexact=billing_details.email,
                    total=total,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    email=billing_details.email,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                for product_id, product_data in json.loads(cart).items():
                    product = Product.objects.get(id=product_id)
                    if isinstance(product_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                        )
                        order_item.save()
            except Exception as error:
                if order:
                    order.delete()
                return HttpResponse(status=500)
        
        self._send_confirmation_email(order)
        return HttpResponse(status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(status=200)
