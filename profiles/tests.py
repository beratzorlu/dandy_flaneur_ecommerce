from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        """
        Creates testuser to test pages with log-in requirements.
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )
        testuser.save()

    def test_profile(self):
        """
        Tests if testuser can access profile page.
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles.html')

    def test_profile_logged_out(self):
        """
        Test if unauthenticated user gets redirected
        if they try to access profile page.
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 302)
