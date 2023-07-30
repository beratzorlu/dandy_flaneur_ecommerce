from django.core import mail
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import UserContactForm
from .views import contact_view


class TestViews(TestCase):
    def setUp(self):
        """
        Creates mock superuser to test site functionality
        with authorization requirements.
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )
        testuser.save()

    def test_contact_page(self):
        """
        Tests if testuser can access contact us page.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')


class TestContactForm(TestCase):
    """
    Tests if post form can be submitted with invalid inputs.
    """
    def test_name_is_required(self):
        form = UserContactForm({'sender_name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('sender_name', form.errors.keys())
        self.assertEqual(form.errors['sender_name'][0],
                         'This field is required.')

    def test_slug_is_required(self):
        form = UserContactForm({'email_address': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(form.errors['email_address'][0],
                         'This field is required.')

    def test_slug_is_required(self):
        form = UserContactForm({'phone_num': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_num', form.errors.keys())
        self.assertEqual(form.errors['phone_num'][0],
                         'This field is required.')

    def test_message_is_required(self):
        form = UserContactForm({'message': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0],
                         'This field is required.')


class ContactViewTestCase(TestCase):
    """
    Tests if user can submit contact us form and be
    redirected to correct template.
    """

    def test_contact_view_success(self):
        url = reverse('contact')

        data = {
            'email_address': 'test@example.com',
            'sender_name': 'Test User',
            'phone_num': '1234567890',
            'message': 'This is a test message.'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
