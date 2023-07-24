from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post


class BlogList(generic.ListView):
    """
    *View for rendering the contact page
    *Paginates after 6 posts
    """
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6
    context_object_name = "blog_list"


class PostDetail(View):
    """
    *View for rendering the content of a blog post.
    *Renders the detailed post page once clicked on
        associated url.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(is_published=True)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(is_published=True)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,

            },
        )
