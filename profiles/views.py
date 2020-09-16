from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .models import UserProfile

from checkout.models import Order
from licenses.models import License

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()
    licenses = profile.licenses.all()

    context = {
        'profile': profile,
        'orders': orders,
        'licenses': licenses,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html' , context)
