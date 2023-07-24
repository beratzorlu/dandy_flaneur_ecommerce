from .models import Comment, Post
from products.widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from django import forms


class PostForm(forms.ModelForm):
    """
    Renders form for editing and publishing new post.
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content',
                  'excerpt', 'image', 'is_published',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    content = forms.CharField(widget=SummernoteWidget())
