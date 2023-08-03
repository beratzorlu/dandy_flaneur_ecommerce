from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Defines the db models for blog posts.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="post_blog")
    is_liked = models.ManyToManyField(User, related_name='post_like',
                                      blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_list')

    def number_of_likes(self):
        return self.is_liked.count()


class Comment(models.Model):
    """
    Defines the db models for comment posts.
    """
    name = models.CharField(max_length=32)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_author', )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.content} | {self.name}"
