from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.paginator import Paginator


class allWorkshops(generic.ListView):
    """ View for rendering the workshops page """

    def get(self, request):
        return render(request, 'workshop/workshop.html')
