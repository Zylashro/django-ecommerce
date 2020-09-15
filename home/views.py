from django.shortcuts import render

from products.models import Product

# Create your views here.

def index(request):
    products = Product.objects.filter(on_sale=True)[:3]
    if products.count() < 1:
        products = Product.objects.order_by('?')[:3]
    
    context = {
        'products': products,
        'range': range(products.count()),
    }

    return render(request, 'home/index.html', context)


def tac(request):
    """ A view to return the tac page """

    return render(request, 'home/tac.html')


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def payment(request):
    """ A view to return the payment page """

    return render(request, 'home/payment.html')


def impressum(request):
    """ A view to return the impressum page """

    return render(request, 'home/impressum.html')


def instructions(request):
    """ A view to return the instructions page """

    return render(request, 'home/instructions.html')


def contact(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')


def support(request):
    """ A view to return the support page """

    return render(request, 'home/support.html')
