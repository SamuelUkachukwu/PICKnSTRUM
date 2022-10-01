from django.shortcuts import render
from .models import Post, PostCategory


# Create your views here.
def blog_home(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    top_stories = PostCategory.objects.filter(name='top_stories').order_by('?')
    context = {
        'posts': posts,
        'on_blog': True,
        'top_stories': top_stories,
    }
    template_name = 'blog/blog_home.html'
    return render(request, template_name, context)


def view_blog_article(request):
    """View to view individual blog posts"""
    pass