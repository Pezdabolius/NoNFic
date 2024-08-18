from django.test import TestCase, Client
from django.urls import reverse
from good.models import Product, Category
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cart_detail = reverse('cart')
        self.checkout = reverse('checkout')
        self.add_cart = reverse('add_cart', args=['prey'])
        self.remove_cart = reverse('remove_cart', args=['prey'])
        self.delete_cart = reverse('delete_cart', args=['prey'])
        self.product = Product.objects.create(
            name='prey',
            slug='prey',
            price='30.00',
            image='prey.jpg',
            category=Category.objects.create(name='fantasy')
        )

    def test_cart_detail_GET(self):
        response = self.client.get(self.cart_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/detail.html')

    def test_checkout_GET(self):
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/checkout.html')

    def test_add_cart_POST(self):
        response = self.client.post(self.add_cart,
                                    {'product': self.product,
                                     'update_quantity': 'update'})
        self.assertEqual(response.status_code, 302)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)]['quantity'], 1)

    def test_remove_cart_POST(self):
        response = self.client.post(self.add_cart,
                                    {'product': self.product,
                                     'update_quantity': 'update'})

        response = self.client.post(self.remove_cart, {'product': self.product,
                                     'update_quantity': 'update'})
        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)

    def test_delete_cart_POST(self):
        response = self.client.post(self.add_cart,
                                    {'product': self.product,
                                     'update_quantity': 'update'})
        response = self.client.post(self.add_cart,
                                    {'product': self.product,
                                     'update_quantity': 'update'})

        response = self.client.post(self.delete_cart, {'product': self.product,
                                     'update_quantity': 'update'})

        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)



