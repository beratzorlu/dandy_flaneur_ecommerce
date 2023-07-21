from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField


class UserContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    phone_num = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353001112233')}))

    class Meta:
        model = Contact
        fields = ('sender_name', 'phone_num', 'email_address', 'message')
