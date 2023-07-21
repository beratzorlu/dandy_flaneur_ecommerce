from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Contact
from .forms import UserContactForm
from store.models import Product, Category


class contactView(View):
    """
    *Displays contact form.
    *checks for saved user data and injects into form.
    *Displays pop-up notification.
    *Sends automated confirmation email.
    """
    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        categories_list = Category.objects.all()

        if request.user.is_authenticated:
            email_address = request.user.email
            user_contact_form = UserContactForm(initial={'email_address': email_address})
        else:
            user_contact_form = UserContactForm()

        context = {
            'categories_list': categories_list,
            'user_contact_form': user_contact_form
        }

        return render(request, 'contact/contact.html',
                      context)

    def post(self, request):
        user_contact_form = UserContactForm(data=request.POST)

        if user_contact_form.is_valid():
            user_contact = user_contact_form.save(commit=False)

            if len(user_contact.message) < 20:
                messages.error(request, 'Message must be at least 20 characters long')
                return render(request, 'contact/contact.html', {'user_contact_form': user_contact_form})

            user_contact.save()

            user_email = user_contact.email_address

            subject = render_to_string('contact/confirmation_emails/conf_email_subj.txt')

            body = render_to_string(
                'contact/confirmation_emails/conf_email_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL}
            )

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=True
            )

            messages.success(request, 'Success! Your message has been sent.')

            return render(request, 'contact/success_contact.html')

        return render(request, 'contact/contact.html', {'user_contact_form': user_contact_form})


def retrieve_user_details(request):
    """
    Queries logged-in user data to check if they have an account.
    """

    account_email = request.user.email
    account_user = User.objects.filter(email=account_email).first()
    return account_user
