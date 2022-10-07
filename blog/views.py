from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
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

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        disliked = True
    template_name = 'blog/post_view.html'
    context = {
        'post': post,
        'posts': posts,
        'cat_list': cat_list,
        "liked": liked,
        "disliked": disliked,
        'on_blog': True,
    }
    return render(request, template_name, context)


class PostLikes(View):
    """this view adds likes to a post
    checks for dislikes and remove it"""
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        for dislikes in post.dislikes.all():
            if dislikes == request.user:
                post.dislikes.remove(request.user)
                break

        liked = False
        for likes in post.likes.all():
            if likes == request.user:
                liked = True
                break
        if not liked:
            post.likes.add(request.user)
        if liked:
            post.likes.remove(request.user)
        return redirect(reverse('view_post', args=[slug]))


class PostDislikes(View):
    """this view adds dislikes to a post
    checks for likes and remove it"""

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        for likes in post.likes.all():
            if likes == request.user:
                post.likes.remove(request.user)
                break

        disliked = False
        for dislikes in post.dislikes.all():
            if dislikes == request.user:
                disliked = True
                break
        if not disliked:
            post.dislikes.add(request.user)
        if disliked:
            post.dislikes.remove(request.user)
        return redirect(reverse('view_post', args=[slug]))
