from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ReviewForm
from . models import Product, Category, Review


# Create your views here.
def all_products(request):
    """ Renders the product template, sorting and search querries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You did not enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail_view(request, product_id):
    """ Renders a detail view of the product"""
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all().order_by('created_on')
    features = product.features.all()

    context = {
        'product': product,
        'reviews': reviews,
        'features': features,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    try:
        review = product.reviews.get(name=request.user)
        if review:
            review_form = ReviewForm(
                request.POST or None,
                instance=review
            )
            if review_form.is_valid():
                review_form.save()
                messages.success(
                    request, f'You have updated your review of {product}.\
                    Thank you for your feed back!')
                return redirect(reverse('product_detail', args=[product.id]))
            template_name = 'products/review.html'
            context = {
                'product': product,
                'review': ReviewForm(),
                'review_form': review_form,
                }
            return render(request, template_name, context)
    except Review.DoesNotExist:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                form = review_form.save(commit=False)
                form.name = request.user
                form.product = product
                review_form.save()
                return redirect(reverse('product_detail', args=[product.id]))
            review_form = ReviewForm()
        return render(request, 'products/review.html', {
            'review_form': ReviewForm(),
            'product': product
            })


def delete_review(request, product_id):
    """This function deletes a selected review"""
    product = get_object_or_404(Product, pk=product_id)
    review_delete = product.reviews.get(name=request.user)
    review_delete.delete()
    return redirect('profile')
