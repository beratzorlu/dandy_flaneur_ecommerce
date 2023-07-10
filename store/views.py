from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.paginator import Paginator


class allProducts(generic.ListView):
    """ View for rendering the store page """

    def get(self, request):
        return render(request, 'store/store_products.html')
