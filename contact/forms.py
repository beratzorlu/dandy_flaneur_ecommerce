from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
   
        placeholders = {
            'sender_name': 'Your Name',
            'phone_num': 'Phone Number',
            'email_address': 'Email Address',
            'message': 'Your Message',
        }

        self.fields['sender_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False

    phone_num = PhoneNumberField(
        error_messages={
            'invalid': 'Please enter a valid phone number in international format (eg. +353 87 000 00 00).',
            'required': 'This field is required.',
        },
    )

    class Meta:
        model = Contact
        fields = ('sender_name', 'phone_num', 'email_address', 'message')
        labels = {
            'sender_name': 'Your Name',
            'phone_num': 'Phone Number',
            'email_address': 'Email Address',
            'message': 'Your Message'
            }
