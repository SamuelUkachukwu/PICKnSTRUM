from django.shortcuts import render
from django.conf import settings


# Create your views here.
def index(request):
    """ Renders the home template """
    return render(request, 'home/index.html')


def about_us(request):
    """presents the about us page"""
    template_name = 'home/connect.html'
    return render(request, template_name)


def contct_us(request):
    """Renders the contact us page"""
    phone = settings.PICKNSTRUM_PHONE
    email = settings.PICKNSTRUM_EMAIL
    address = settings.PICKNSTRUM_ADDRESS
    context = {
        'phone': phone,
        'email': email,
        'address': address
    }
    template_name = 'home/connect.html'
    return render(request, template_name, context)