from store.widgets import CustomClearableFileInput
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from django import forms


class BlogForm(forms.ModelForm):
    """
    Renders form for publishing a post.
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
    Renders form for editing a post.
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


class CommentForm(forms.ModelForm):
    """
    Renders form for editing and publishing a post.
    """
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = False

    class Meta:
        model = Comment
        fields = ('content', )


class CommentEditForm(forms.ModelForm):
    """
    Renders form for editing and publishing a post.
    """
    def __init__(self, *args, **kwargs):
        super(CommentEditForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = False

    class Meta:
        model = Comment
        fields = ('content', )

    content = forms.CharField(widget=SummernoteWidget())