from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.db.models import Q  # is used to generate a search query
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ItemForm


def products_list(request):
    """View for listing all products and sorting."""

    products = Product.objects.all()
    all_categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'category':
                sort_key = 'category__name'
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please input search criteria")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'all_categories': all_categories,
        'search_term': query,
        'current_sort': current_sort
    }

    return render(request, 'store/store_products.html', context)


def store_detail(request, product_id):
    """Shows detailed information of a chosen product item"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/store_detail.html', context)


@login_required
def add_store(request):
    """Add new product object to store"""

    if not request.user.is_superuser:
        messages.error(request, 'You do not have administrator previliges to perform this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New product added to store successfully.')
            return redirect(reverse('store_detail', args=[product.id]))
        else:
            messages.error(request, 'A problem occured when trying to add new product. Please ensure details are correct.')
    else:
        form = ItemForm()

    template = 'store/add_store.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
