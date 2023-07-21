from django.contrib import admin
from daterangefilter.filters import DateRangeFilter
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('user', 'sender_name', 'email_address',
                   'phone_num', 'date_created')
    list_display = ('form_id', 'user', 'sender_name',
                    'message', 'phone_num', 'date_created')

    search_fields = ['sender_name']
    list_filter = (('sender_name', DateRangeFilter),)
