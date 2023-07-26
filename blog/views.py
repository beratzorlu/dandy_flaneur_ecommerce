from django.views import generic, View
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import BlogForm


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


class AddBlog(LoginRequiredMixin, generic.CreateView):
    """
    Class-based view for creating new blog posts.
    """
    model = Post
    template_name = 'blog/blog_add.html'
    form_class = BlogForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        if user.is_authenticated:
            messages.success(self.request, "Success! Your blog has been \
                                            submitted.")
            return super(AddBlog, self).form_valid(form)
        else:
            messages.warning(self.request, "You do not have the privileges to \
                                            perform this action")
            return HttpResponseRedirect(reverse('blog_list'))
