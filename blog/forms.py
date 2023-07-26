from .models import Post
from store.widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from django import forms


class BlogForm(forms.ModelForm):
    """
    Renders form for editing and publishing a post.
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content',
                  'excerpt', 'image', 'is_published')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    content = forms.CharField(widget=SummernoteWidget())
