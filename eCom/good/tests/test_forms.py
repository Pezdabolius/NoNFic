from django.test import TestCase
from good.forms import ReviewForm


class FormsTest(TestCase):
    def test_form_valid_data(self):
        form = ReviewForm(data={
            'title': 'Car',
            'body': "It's greate car!"
        })
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)