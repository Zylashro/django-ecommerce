from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile

from checkout.models import Order

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    context = {
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, context)

def order_history(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, context)
