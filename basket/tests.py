import unittest
from django.test import Client, TestCase
from .views import view_basket
from store.models import Product, Category


class TestViews(TestCase):
    def test_basket_view(self):
        """
        Tests if testuser can access the basket page.
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
