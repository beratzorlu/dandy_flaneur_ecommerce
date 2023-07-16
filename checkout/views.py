from django.shortcuts import (render, redirect, reverse, get_object_or_404,
                              HttpResponse)
from .forms import OrderForm


def checkout_data_cache(request):
    pass


def storeCheckout(request):
    """Renders checkout form page and logic"""

    template = 'checkout/checkout.html'
    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
