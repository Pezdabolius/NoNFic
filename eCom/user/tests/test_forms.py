from django.test import TestCase
from user.forms import LoginForm, RegistrationForm


class FormsTest(TestCase):
    def test_form_valid_data(self):
        form_log = LoginForm(data={
            'username': 'admin',
            'password': 'defender'
        })
        form_reg = RegistrationForm(data={
            'username': 'kick',
            'email': 'kuddeijoirasso-4202@yopmail.com',
            'password': 'defender27',
            'rep_password': 'defender27',
            'conditions': 'True'
        })
        self.assertTrue(form_log.is_valid())
        self.assertTrue(form_reg.is_valid())

    def test_form_no_data(self):
        form_log = LoginForm(data={})
        self.assertFalse(form_log.is_valid())