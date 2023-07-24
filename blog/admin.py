from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('author', 'title', 'slug', 'created_on', 'is_published')
    list_filter = ('author', 'is_published', 'created_on', 'is_published')
