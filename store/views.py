from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.db.models import Q  # is used to generate a search query
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ItemForm


class ProductListView(ListView):
    """
    *Displays store product cards in a list format.
    *Allows for content sorting and searching.
    *Paginates content 10 products per page.
    """
    model = Product
    template_name = 'store/store_products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        products = Product.objects.all()
        query = self.request.GET.get('q')
        category = self.request.GET.getlist('category')
        sort_key = self.request.GET.get('sort')
        direction = self.request.GET.get('direction')

        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query) | Q(artist__icontains=query)
            products = products.filter(queries)

        if category:
            products = products.filter(category__name__in=category)

        if sort_key:
            if sort_key == 'category':
                sort_key = 'category__name'
            if sort_key == 'name':
                sort_key = 'name_lower'
                products = products.annotate(name_lower=Lower('name'))
            if direction == 'desc':
                sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['search_term'] = self.request.GET.get('q', '')
        context['current_sort'] = f"{self.request.GET.get('sort', '')}_{self.request.GET.get('direction', '')}"
        
        return context


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
            if 'rating' in form.errors:
                messages.error(request, form.errors['rating'][0])
            else: 
                messages.error(request, 'A problem occured when trying to add new item. Please ensure details are correct.')
    else:
        form = ItemForm()

    template = 'store/add_store.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_store(request, product_id):
    """Delete product from store"""

    if not request.user.is_superuser:
        messages.error(request, 'You do not have administrator previliges to perform this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product (ID: {product.id}) successfully deleted!')
    return redirect(reverse('store'))


@login_required
def edit_store(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'You do not have administrator previliges to perform this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item edit form submitted successfully.')
            return redirect(reverse('store_detail', args=[product.id]))
        else:
            messages.error(request, 'A problem occured when trying to edit item. Please ensure details are valid.')
    else:
        form = ItemForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'store/edit_store.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
