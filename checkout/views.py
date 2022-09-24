from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages


# Create your views here.
def checkout(request):
    """Renders the checkout page"""
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Shopping Cart is currently Empty")
        return redirect(reverse('products'))
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'publishable_key': 'pk_test_51LcIJvIQDXjp8otbGZdOBifdz7sUeNxwfMkjkzndAxjjxOi5LZc9fsD9Uu5wSqBwd9OFIg35Zvr0APR2hg7e877X00LSVa7j7O',
        'client_secret': 'client secret yeah long'
    }
    return render(request, 'checkout/checkout.html', context)
