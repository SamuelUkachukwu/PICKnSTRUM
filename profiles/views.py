from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from checkout.models import Order
from products.models import Review
from .models import UserProfile

from .forms import UserProfileForm, ProfileImageForm


# Create your views here.
@login_required
def profile(request):
    """Renders the profile page"""
    profile = get_object_or_404(UserProfile, user=request.user)
    reviews = Review.objects.filter(name=request.user).order_by("-created_on")
    image_form = ProfileImageForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )
    if image_form.is_valid():
        image_form.save()
        return redirect('profile')
    orders = profile.orders.all().order_by("-date")
    context = {
        'profile': profile,
        'orders': orders,
        'image_form': image_form,
        'reviews': reviews,
        'profile_page': True
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request):
    """Profile address update view"""
    profile = get_object_or_404(UserProfile, user=request.user)
    address_form = UserProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )
    if address_form.is_valid():
        address_form.save()
        messages.success(
            request,
            'Your Profile Address has been updated successfully')
        return redirect('profile')
    context = {
        'address_form': address_form,
        'profile': profile,
        'profile_page': True
    }
    return render(request, 'profiles/update_address.html', context)


@login_required
def order_history(request, order_number):
    """Retrieve the order from the order app"""
    order = get_object_or_404(Order, order_number=order_number)
    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, 'checkout/checkout_success.html', context)
