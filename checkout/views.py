from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST

from django.conf import settings
from django.contrib import messages

from cart.contexts import cart_contents
from products.models import Product
from profiles.models import UserProfile

from profiles.forms import UserProfileForm
from .forms import OrderForm

from .models import Order, OrderLineItem


import stripe
import json


# Create your views here.
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save-dlv-info': request.POST.get('save-dlv-info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Renders the checkout page"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "A Product in your cart was not found in our database"
                        f"Please call {settings.PICKNSTRUM_PHONE} for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_dlv_info'] = 'save-dlv-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'An Error occured with your form \
                Please verify your information')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your Shopping Cart is currently Empty")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """Successful checkout handler"""

    save_dlv_info = request.session.get('save_dlv_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_dlv_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your Order: {order_number} has been processed!\
        A confirmation email will be sent to {order.email}')
    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
