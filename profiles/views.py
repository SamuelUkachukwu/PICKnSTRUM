from django.shortcuts import render


# Create your views here.
def profile(request):
    """Renders the profile page"""
    context = {}
    return render(request, 'profiles/profile.html', context)