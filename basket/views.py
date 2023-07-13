from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from store.models import Product


def view_basket(request):
    """Renders the basket contents page"""

    return render(request, 'basket/basket.html')
