from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import ItemForm


class TestViews(TestCase):
    def setUp(self):
        """
        Creates testuser to test pages where
        you need to be logged in to view.
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )
        testuser.save()

        self.client = Client()
        self.product_list_url = reverse('store')

    def test_product_list(self):
        """
        Tests if testuser can access products page.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store_products.html')

    def test_add_product(self):
        """
        Tests if testuser gets redirected to homepage when
        trying to add without admin authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/store/add_store')
        self.assertEqual(response.status_code, 301)

    def test_edit_product(self):
        """
        Tests if testuser gets redirected to homepage when
        trying to edit without admin authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/store/edit_store/1')
        self.assertEqual(response.status_code, 301)

    def test_delete_product(self):
        """
        Tests if testuser gets redirected to homepage when
        trying to delete without admin authorization.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/store/delete_store/1')
        self.assertEqual(response.status_code, 301)


class TestItemForm(TestCase):
    """
    Tests form submission against submission of invalid form data.
    """

    def test_name_is_required(self):
        form = ItemForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ItemForm({'description': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description']
                         [0], 'This field is required.')

    def test_price_is_required(self):
        form = ItemForm({'price': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')
