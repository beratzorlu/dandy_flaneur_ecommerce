from django.views import generic, View
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .forms import BlogForm


class BlogList(generic.ListView):
    """
    *View for rendering the contact page.
    *Paginates after 6 posts.
    *Retrieves context data.
    *Checks if the active user is a superuser.
    *Filters unpublished posts and returns this data to context.
    """
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6
    context_object_name = "blog_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_superuser:

            unpublished_posts = Post.objects.filter(is_published=False)

            context['unpublished_posts'] = unpublished_posts

        return context


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
    *Check if form is valid.
    *Check if user is logged in.
    *If succesful, use get_absolute_url setting from model.
    *Else, display error and return to blog list page.
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
            messages.error(self.request, "You do not have the privileges to \
                                            perform this action")
            return HttpResponseRedirect(reverse('blog_list'))


class DeleteBlog(LoginRequiredMixin, generic.DeleteView):
    """
    *Check if user has permission to delete blog post.
    *Get filtered queryset for view showing only published posts.
    *Handle deletion of blog post.
    """
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser  # noqa

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(is_published=True)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            messages.success(self.request, 'Success! Blog has been successfully deleted.')  # noqa
            return super(DeleteBlog, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, "You do not have the privileges to \
                                            perform this action")
            return HttpResponseForbidden()
