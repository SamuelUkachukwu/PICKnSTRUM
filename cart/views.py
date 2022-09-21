from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.
def view_cart(request):
    """ Renders the shopping cart content page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add Product Items To Cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, item_id):
    """update the quantity of items in cart"""
    # product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    print('THIS IS:', quantity)

    if item_id in list(cart.keys()):
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    cart = request.session.get('cart', {})
    try:
        cart.pop(item_id)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        print('THIS IS:', e)
        return HttpResponse(status=500)
