from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.models import Post
from products.models import Product

from .forms import ProductForm, AddPostForm


# Create your views here.
@login_required
def management(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    paginator = Paginator(
        Post.objects.all().order_by("-created_on"), 4)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
    }
    template_name = 'management/storekeep.html'
    return render(request, template_name, context)


@login_required
def add_product(request):
    """Add a product to a database"""
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product Added Successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Error adding the product. \
                Verify that all fields are filled in accurately.')
    else:
        form = ProductForm()

    template_name = 'management/data-entry-product.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def edit_product(request, product_id):
    """ modify a product in the database """
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Product update failed. \
                    Please verify that the form is accurate.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template_name = 'management/data-entry-product.html'
    context = {
        'product': product,
        'form': form,
        'edit': True,

    }
    return render(request, template_name, context)


@login_required
def delete_product(request, product_id):
    """ Remove a product from the database."""
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect(reverse('products'))


@login_required
def add_post(request):
    """Add a post to the database"""
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Post Added Successfully!')
            return redirect(reverse('management'))
        else:
            messages.error(request, 'Error adding the post. \
                Verify that all fields are filled in accurately.')
    else:
        form = AddPostForm()

    template_name = 'management/data-entry-post.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def edit_post(request, slug):
    """ modify a product in the database """
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully updated!')
            return redirect(reverse('management'))
        else:
            messages.error(
                request, 'Post update failed. \
                    Please verify that the form is accurate.')
    else:
        form = AddPostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template_name = 'management/data-entry-post.html'
    context = {
        'post': post,
        'form': form,
        'edit_post': True,

    }
    return render(request, template_name, context)


@login_required
def delete_post(request, slug):
    """ Remove a post from the database."""
    if not request.user.is_superuser:
        messages.error(
            request, 'Only store owners are permitted to take this action.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post successfully deleted!')
    return redirect(reverse('management'))
