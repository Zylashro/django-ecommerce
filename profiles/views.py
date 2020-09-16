# from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from .forms import UserLoginForm

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

"""
def profile_login(request, red):

    redirect_url = reverse('profile')
    if red:
        redirect_url = red

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                if request.POST['redirect_url']:
                    redirect_url = request.POST['redirect_url']
                return redirect(redirect_url)
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    context = {
        'login_form': login_form,
        'redirect_url': redirect_url,
    }

    return render(request, 'profiles/login.html', context)
"""
    
    