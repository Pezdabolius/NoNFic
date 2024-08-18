from django.test import TestCase, Client
from django.urls import reverse
from good.models import Product, Category, Review
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('products_list')
        self.product = Product.objects.create(
            name='prey',
            slug='prey',
            price='30.00',
            image='prey.jpg',
            category=Category.objects.create(name='fantasy')
        )
        self.user = User.objects.create_user(username='admin', password='defender', email='kuddeijoirasso-4202@yopmail.com')
        self.review = Review.objects.create(product=self.product, user=self.user,
                              title='Tomate', body='Pasta with tomate')
        self.detail_url = reverse('product_detail', args=['prey'])
        self.client.login(username='admin', password='defender')

    def test_products_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/list_products.html')

    def test_product_detail_GET(self):
        product = self.product
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/detail_product.html')

    def test_review_GET(self):
        review = self.review
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/detail_product.html')

    def test_review_POST(self):
        response = self.client.post(self.detail_url, {
            'product': self.product, 'user': self.user,
            'title': 'Car', 'body': "It's greate car!"})
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.count_reviews, 1)

