from store.widgets import CustomClearableFileInput
from .models import Post
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

    widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
            'content': forms.Textarea(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    content = forms.CharField(widget=SummernoteWidget())


class EditForm(forms.ModelForm):
    """
    Defines the model for the blog edit form
    """
    class Meta:
        model = Post
        fields = ('is_published', 'title', 'excerpt', 'content', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
            'content': forms.Textarea(attrs={'class': 'mb-4 rounded-0 dandy-border form-control'}),
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    content = forms.CharField(widget=SummernoteWidget())
