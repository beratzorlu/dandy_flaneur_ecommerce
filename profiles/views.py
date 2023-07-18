from django.shortcuts import render

from django.shortcuts import render


def profiles(request):
    """ Display the user's profile. """

    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
