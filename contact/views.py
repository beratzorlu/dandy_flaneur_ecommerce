from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserContactForm
from store.models import Product, Category


class contactView(View):
    """ View for rending the contact u page """

    """
    This view displays the contact form and if the user
    is registered and inserts the user email into the
    email field
    """
    template_name = 'contact/contact.html'
    success_message = 'Success! Your message has been sent.'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        categories_list = Category.objects.all()

        if request.user.is_authenticated:
            user_email = request.user.email
            user_contact_form = UserContactForm(initial={'user_email': user_email})
        else:
            user_contact_form = UserContactForm()

        context = {
            'categories_list': categories_list,
            'user_contact_form': user_contact_form
        }

        return render(request, 'contact/contact.html',
                      context)

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        user_contact_form = UserContactForm(data=request.POST)

        if user_contact_form.is_valid():
            user_contact = user_contact_form.save(commit=False)
            if len(user_contact.message) < 20:
                messages.error(
                    request, 'Message must be at least 20 characters long')
                return render(
                    request,
                    'contact/contact.html',
                    {
                        'user_contact_form': user_contact_form
                    }
                )

            user_contact.user = request.user
            user_contact.save()
            messages.success(
                request, "Success! Your message has been sent")
            return render(request, 'contact/received.html')

        return render(request, 'contact/contact.html',
                      {'user_contact_form': user_contact_form})


def retrieve_user_details(request):
    """
    Queries logged-in user data if they have an account.
    """

    account_email = request.user.email
    account_user = User.objects.filter(email=account_email).first()
    return account_user
