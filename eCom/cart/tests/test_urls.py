from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import *


class UrlsTest(TestCase):

    def test_cart_urls(self):
        response = reverse('cart')
        self.assertEqual(resolve(response).func, cart_detail)

    def test_checkout_urls(self):
        response = reverse('checkout')
        self.assertEqual(resolve(response).func, order)

    def test_add_remove_delete_urls(self):
        response_add = reverse('add_cart', args=['slug'])
        self.assertEqual(resolve(response_add).func, add_cart)

        response_remove = reverse('remove_cart', args=['slug'])
        self.assertEqual(resolve(response_remove).func, remove_cart)

        response_delete = reverse('delete_cart', args=['slug'])
        self.assertEqual(resolve(response_delete ).func, delete_cart)
