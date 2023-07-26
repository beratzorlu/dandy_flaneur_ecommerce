from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe
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


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ('name', 'author', 'content')
    list_display = ('author', 'name', 'post', 'content_field', 'created_on', 'is_approved')
    list_filter = ('name', 'post', 'author', 'content', 'created_on', 'is_approved')

    def content_field(self, obj):
        return mark_safe(obj.content)

    content_field.short_description = 'Content'
