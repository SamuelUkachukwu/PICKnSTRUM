from django.shortcuts import render


# Create your views here.
def management(request):
    template_name = 'management/storekeep.html'
    return render(request, template_name)
