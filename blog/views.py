from django.shortcuts import render


# Create your views here.
def blog_home(request):
    context = {
        'on_blog': True
    }
    template_name = 'blog/blog_home.html'
    return render(request, template_name, context)
