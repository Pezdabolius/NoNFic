from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.registration_url = reverse('registration')

    def test_login_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'admin',
            'password': 'defender'
        })
        self.assertEqual(response.status_code, 302)

    def test_registration_POST(self):
        response = self.client.post(self.registration_url, {
            'username': 'kick',
            'password': 'defender',
            'rep_password': 'defender'
        })
        self.assertEqual(response.status_code, 302)
