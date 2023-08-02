from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import BlogForm, EditForm, CommentForm, CommentEditForm


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
    paginate_by = 8
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
        comments = post.comments.filter(is_approved=True).order_by("-created_on")
        is_liked = False

        if post.is_liked.filter(id=self.request.user.id).exists():
            is_liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "is_liked": is_liked,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(is_published=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(is_approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        is_liked = False

        if post.is_liked.filter(id=self.request.user.id).exists():
            is_liked = True

        if comment_form.is_valid():
            comment_form.instance.author = self.request.user
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            commented = True
            error_message = None
            messages.success(request, "Success! Your comment has been \
                                        submitted for admin review.")
        else:
            commented = False
            error_message = "It looks like there is an issue with the \
                            submitted content. Please ensure the form \
                            is valid."
            messages.error(request, "Looks like something went wrong. Please \
                                        try again.")

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "is_liked": is_liked,
                "comments": comments,
                "commented": commented,
                "comment_form": CommentForm(),
                "error_message": error_message,
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
        return self.request.user == post.author or self.request.user.is_superuser

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(is_published=True)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            messages.success(self.request, 'Success! Blog has been successfully deleted.')
            return super(DeleteBlog, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, "You do not have the privileges to \
                                            perform this action")
            return HttpResponseForbidden()


class EditBlog(LoginRequiredMixin, generic.UpdateView):
    """
    *Get Post object from the instance.
    *Filter data to only include published posts.
    *Check if edit blog form is valid.
    *Check if user is adequately authenticated.
    *Save edits and redirect to blog list page.
    *Else, display error message and reverse to homepage.
    """
    model = Post
    template_name = 'blog/blog_edit.html'
    form_class = EditForm
    success_url = reverse_lazy('blog_list')

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(is_published=1)

    def form_valid(self, form):
        blogObject = self.get_object()
        post = form.save(commit=False)
        if self.request.user == post.author or self.request.user.is_superuser:
            post.save()
            messages.success(self.request, 'Success! Your changes have been \
                                            saved.')
            return redirect(reverse("blog_list"))
        else:
            messages.warning(self.request, 'You are not authorized to edit \
                                            the posts of other users.')
            return redirect(reverse("home"))


class LikeBlog(View):
    """
    *Get Post object from the instance.
    *Check if the blog post is liked already.
    *If so, toggle liked to unliked once clicked.
    *Otherwise, add a like to the blog post.
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.is_liked.filter(id=request.user.id).exists():
            post.is_liked.remove(request.user)
            messages.info(request, 'You removed your like.')
        else:
            post.is_liked.add(request.user)
            messages.success(request, 'You liked this post.')

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))


@login_required
def comment_edit(request, comment_id):
    """
    *Check if the edit form is valid.
    *If so, save the data input by the user.
        -Display success message
        -Redirect to detail page.
    *Otherwise, display an error message.
    """
    template = "blog/blog_comments_edit.html"
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    comment_form = CommentEditForm(request.POST or None, instance=comment)

    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Successfully saved your changes.")
            return redirect(reverse("blog_detail", args=[comment.post.slug]))
        messages.error(request, "Sorry, something went wrong. Please try \
                                    again.")

    context = {
        "comment": comment,
        "comment_form": comment_form,
    }

    return render(request, template, context)


@login_required
def comment_delete(request, comment_id):
    """
    *Check if the name attribute of the comment
        matches the username of the user.
    *If so, remove the comment from the database
        and display success message.
    *Otherwise, display an error message and redirect
        users to homepage.
    """
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if comment.name == request.user.username:
        comment.delete()
        messages.success(request, "You have successfully deleted your \
                                    comment.")
        return redirect(reverse("blog_detail", args=[comment.post.slug]))
    else:
        messages.error(request, "Looks like something went wrong.")
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))
