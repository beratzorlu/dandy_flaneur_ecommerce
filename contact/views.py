from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import ContactForm
from .forms import UserContactForm
from store.models import Product, Category


def contact_view(request):
    """ Handle contact form """
    if request.method == 'POST':
        user_contact_form = UserContactForm(request.POST)
        if user_contact_form.is_valid():
            complete_form = user_contact_form.save()
            messages.info(request, 'Your message was successfuly sent!')

            """Send the user a confirmation email"""
            user_email = complete_form.email_address
            subject = render_to_string(
                'contact/confirmation_emails/conf_email_subj.txt')
            body = render_to_string(
                'contact/confirmation_emails/conf_email_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return render(request, 'contact/success_contact.html')
        else:
            messages.error(request, 'Looks like something went wrong. \
            Please try again.')
    else:
        user_contact_form = UserContactForm()

    template = 'contact/contact.html'
    context = {
        'user_contact_form': user_contact_form,
    }

    return render(request, template, context)
