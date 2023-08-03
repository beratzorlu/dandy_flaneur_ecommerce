from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import AccountProfile
from .forms import AccountProfileForm
from checkout.models import Order


def profiles(request):
    """
    Display the user's profile.
    """
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


def account_order_history(request, order_number):
    """
    Queries the previous purchases of the user.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
