from django.test import TestCase
from django.urls import reverse, resolve
from user.views import login_user, logout_user, registration_user


class UrlsTest(TestCase):
    def test_login_user_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_user)

    def test_logout_user_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_registration_user_url(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration_user)