from django.shortcuts import render, get_object_or_404
from . models import Product


# Create your views here.
def all_products(request):
    """ Renders the product template, sorting and search querries"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail_view(request, product_id):
    """ Renders a detail view of the product"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
