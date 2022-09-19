from django.shortcuts import render


# Create your views here.
def view_cart(request):
    """ Renders the shopping cart content page """
    return render(request, 'cart/cart.html')
