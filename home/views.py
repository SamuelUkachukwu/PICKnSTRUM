from django.shortcuts import render


# Create your views here.
def index(request):
    """ Renders the home template """
    return render(request, 'home/index.html')
