from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import AccountProfile
from .forms import AccountProfileForm


def profiles(request):
    """ Display the user's profile. """
    profiles = get_object_or_404(AccountProfile, user=request.user)

    if request.method == 'POST':
        form = AccountProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = AccountProfileForm(instance=profiles)
    orders = profiles.orders.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)
