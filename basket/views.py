from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from store.models import Product, Category


def view_basket(request):
    """Renders the basket contents page"""

    products = Product.objects.all()
    all_categories = Category.objects.all()

    context = {
        'products': products,
        'all_categories': all_categories
    }

    return render(request, 'basket/basket.html')
