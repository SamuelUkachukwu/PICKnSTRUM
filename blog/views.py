from django.shortcuts import render


# Create your views here.
def blog_home(request):
    context = {}
    template_name = 'blog/blog_home.html'
    return render(request, template_name, context)
