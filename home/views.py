from django.shortcuts import render

# Create your views here.


def home(request):
    """ View for rending the home page """
    return render(request, 'home/index.html')
