from django.conf import settings
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .forms import OrderForm
from .models import Order, OrderLineItem
from store.models import Product
from profiles.models import AccountProfile


class TestOrderForm(TestCase):
    """
    Tests if order form can be submitted with invalid data.
    """

    def test_full_name_is_required(self):
        form = OrderForm({'full_name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name']
                         [0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({'email': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        form = OrderForm({'phone_number': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number']
                         [0], 'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({'street_address1': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1']
                         [0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city']
                         [0], 'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({'country': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')


class CheckoutTestCase(TestCase):
    """
    Tests if the checkout functionality works as expected.
    """
    def setUp(self):
        """
        Creates a mock testuser with access to Stripe functionality.
        """
        self.client = Client()
        self.stripe_public_key = settings.STRIPE_PUBLIC_KEY
        self.stripe_secret_key = settings.STRIPE_SECRET_KEY
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.force_login(self.user)

    def test_store_checkout_get(self):
        """
        Tests if testuser can add items to basket and checkout from store.
        """
        basket = self.client.session.get('basket', {})
        basket['1'] = 2
        self.client.session['basket'] = basket
        self.client.session.save()

        response = self.client.get(reverse('store_checkout'))
        while response.status_code in [301, 302]:
            redirect_url = response.url
            response = self.client.get(redirect_url)

        self.assertEqual(response.status_code, 200)

    def test_checkout_success(self):
        """
        Tests if testsuser's checkout form data is collected as a
        part of the order and the success page rendered.
        """
        order = Order.objects.create(
            full_name='Sinead O Connor',
            email='sineadoconner@forever.com',
            phone_number='1234567890',
            country='IE',
            eircode='12345',
            town_or_city='Dublin',
            street_address1='476 Howth Rd',
            street_address2='Dublin 5',
            county='D',
            order_number='12345',
        )

        response = self.client.get(reverse('checkout_success',
                                   args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
