from django.test import TestCase


class TestViews(TestCase):
    def test_profile(self):
        """
        Tests if homepage renders correctly.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
