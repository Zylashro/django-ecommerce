from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


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
