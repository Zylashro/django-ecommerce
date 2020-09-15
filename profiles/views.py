from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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

    return render(request, 'profile/' , context)

def order_history(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, context)

def licenses_owned(request, id):
    license = get_object_or_404(License, id=id)

    context = {
        'license': license,
        'from_profile': True
    }

    return render(request, context)

@login_required
def change_password(request, *args, **kwargs):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password successfully updated!')
            return redirect(reverse('profile'))
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }

    return render(request, 'password/change_password.html', context)
