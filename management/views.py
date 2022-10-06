from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post
from products.models import Product


# Create your views here.
def management(request):

    paginator = Paginator(
        Post.objects.all().order_by("-created_on"), 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
    }
    template_name = 'management/storekeep.html'
    return render(request, template_name, context)
