from django.shortcuts import render
from . models import Product, ProductFeature


# Create your views here.
def all_products(request):
    """ Renders the product template, sorting and search querries"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
