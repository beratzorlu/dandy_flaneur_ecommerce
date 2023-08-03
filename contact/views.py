from django.conf import settings
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import ContactForm
from .forms import UserContactForm
from profiles.models import AccountProfile
from store.models import Product, Category


def send_email_confirmation(complete_form):
    """
    Handles the confirmation email evet.
    *Defines the subject and body content of the email.
    *Utilizes Django email framework to target and send
        an email to the specified email address.
    """
    user_email = complete_form.email_address

    subject = render_to_string('contact/confirmation_emails/conf_email_subj.txt')  # noqa
    body = render_to_string('contact/confirmation_emails/conf_email_body.txt',
                            {'contact_email': settings.DEFAULT_FROM_EMAIL,
                             'complete_form': complete_form}
                            )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [user_email]
    )


def contact_view(request):
    """
        *Handles user contact form.
        *It will prepopulate form with preexisting user data.
        *If not, it will present an empty form.
    """
    user = request.user
    complete_form = None

    if user.is_authenticated:
        profile = get_object_or_404(AccountProfile, user=user)
    else:
        profile = None

    if request.method == 'POST':

        user_contact_form = UserContactForm(request.POST)

        if user.is_authenticated:
            if user_contact_form.is_valid():
                complete_form = user_contact_form.save(commit=False)
                complete_form.user = request.user
                complete_form.save()

                messages.info(request, 'Your message was successfuly sent!')

                send_email_confirmation(complete_form)

                return render(request, 'contact/success_contact.html')

        if not user.is_authenticated:
            if user_contact_form.is_valid():
                complete_form = user_contact_form.save()
                messages.info(request, 'Your message was successfuly sent!')

                send_email_confirmation(complete_form)

                return render(request, 'contact/success_contact.html')
        else:
            messages.error(request, 'Looks like something went wrong. \
                                     Please try again.')
    else:
        user_contact_form = UserContactForm(initial={
            'email_address': user.email if user.is_authenticated else '',
            'sender_name': user.username if user.is_authenticated else '',
            'phone_num': profile.default_phone_number if user.is_authenticated else ''  # noqa
        })

    template = 'contact/contact.html'
    context = {
        'user_contact_form': user_contact_form,
        'complete_form': complete_form,
        'profile': profile,
    }

    return render(request, template, context)
