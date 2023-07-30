
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import BlogForm, CommentForm


class TestBlogForm(TestCase):
    """
    Tests if post form can be submitted with invalid inputs.
    """
    def test_title_is_required(self):
        form = BlogForm({'title': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = BlogForm({'slug': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_content_is_required(self):
        form = BlogForm({'content': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_excerpt_is_required(self):
        form = BlogForm({'excerpt': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('excerpt', form.errors.keys())
        self.assertEqual(form.errors['excerpt'][0], 'This field is required.')


class TestCommentForm(TestCase):
    """
    Tests if comment form can be submitted with invalid inputs.
    """
    def test_comment_is_required(self):
        form = CommentForm({'content': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')


class TestViews(TestCase):
    def setUp(self):
        """
        Create mock superuser to test site functionality
        with authorization requirements.
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )

        testuser.save()

        blog = Post.objects.create(
            title='Test Blog',
            content='Test content',
            author=testuser
        )

        blog.save()

    def test_blog_list(self):
        """
        Tests if non-admin testuser can access blog list page.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_add_blog(self):
        """
        Tests if non-admin testuser gets redirected to 301
        when attempting to add blog without authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/add')
        self.assertEqual(response.status_code, 301)

    def test_edit_blog(self):
        """
        Testss if non-admin testuser gets redirected to 404
        when attempting to edit blog without authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('blog/test-post/edit')
        self.assertEqual(response.status_code, 404)

    def test_delete_blog(self):
        """
        Tests if non-admin testuser gets redirected to 404
        when attempting to delete blog without authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('blog/test-post/delete')
        self.assertEqual(response.status_code, 404)
