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

    def make_published(modeladmin, request, queryset):
        queryset.update(is_published=True)
    
    def make_unpublished(modeladmin, request, queryset):
        queryset.update(is_published=False)
        
    make_published.short_description = "Publish"
    make_unpublished.short_description = "Unpublish"

    actions = [make_published, make_unpublished]
