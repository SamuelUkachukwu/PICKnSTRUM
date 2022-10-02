from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, PostCategory


# Create your views here.
def blog_home(request):
    paginator = Paginator(
        Post.objects.filter(status=1).order_by("-created_on"), 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    query = PostCategory.objects.get(name='top_stories')
    top_stories = Post.objects.filter(category=query).order_by('?')
    context = {
        'posts': posts,
        'on_blog': True,
        'top_stories': top_stories,
    }
    template_name = 'blog/blog_home.html'
    return render(request, template_name, context)


def view_blog_article(request, slug):
    """View to view individual blog posts"""
    paginator = Paginator(
        Post.objects.filter(status=1).order_by("?"), 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    cat_list = PostCategory.objects.all()

    template_name = 'blog/post_view.html'
    context = {
        'post': post,
        'posts': posts,
        'cat_list': cat_list,
        'on_blog': True,
    }
    return render(request, template_name, context)