from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class ContactForm(models.Model):
    """
    Defines the db models for user contact form submissions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="form_contact_user", null=True)
    form_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    sender_name = models.CharField(max_length=50, null=True)
    email_address = models.EmailField(max_length=254, default="")
    phone_num = PhoneNumberField(null=True)
    message = models.TextField()

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.sender_name
