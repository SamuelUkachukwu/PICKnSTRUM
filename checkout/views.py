from django.shortcuts import render


# Create your views here.
def checkout(request):
    """Renders the checkout page"""
    return render(request, 'checkout/checkout.html')
