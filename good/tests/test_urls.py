from django.test import TestCase
from django.urls import reverse, resolve
from good.views import best_selling, product_detail


class UrlsTest(TestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, best_selling)

    def test_product_detail_url(self):
        url = reverse('product_detail', args=['slug'])
        self.assertEqual(resolve(url).func, product_detail)