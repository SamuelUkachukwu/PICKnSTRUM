from django.shortcuts import render


# Create your views here.
def all_products(request):
    """ Renders the home template """
    context = {}
    return render(request, 'products/products.html', context)