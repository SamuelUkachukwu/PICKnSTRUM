from django.shortcuts import render
from django.conf import settings
from .forms import ContactUsForm


# Create your views here.
def index(request):
    """ Renders the home template """
    return render(request, 'home/index.html')


def about_us(request):
    """presents the about us page"""
    template_name = 'home/connect.html'
    return render(request, template_name)


def contact_us(request):
    """Renders the contact us page"""
    phone = settings.DEFAULT_FROM_PHONE
    email = settings.DEFAULT_FROM_EMAIL
    address = settings.DEFAULT_FROM_ADDRESS
    form = ContactUsForm()
    context = {
        'phone': phone,
        'email': email,
        'address': address,
        'form': form,
        'contact_us': True
    }
    template_name = 'home/connect.html'
    return render(request, template_name, context)
