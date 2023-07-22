from django.contrib import admin
from daterangefilter.filters import DateRangeFilter
from .models import ContactForm


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('user', 'sender_name', 'email_address',
                   'phone_num', 'date_created')

    list_display = ('form_id', 'user', 'sender_name',
                    'message', 'phone_num', 'date_created')

    search_fields = ['date_created', 'sender_name']

    list_filter = (('date_created', DateRangeFilter), 'sender_name', 'user')

    list_display_links = ('form_id', 'user', 'sender_name',
                          'message', 'phone_num', 'date_created')
