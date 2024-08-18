from django import forms
from .models import Order


class CartQuantityForm(forms.Form):
    update = forms.BooleanField(initial=False, required=False,
                                widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'country',
                  'city', 'address', 'postal_code')
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                   'country': forms.TextInput(attrs={'placeholder': 'Country'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'address': forms.TextInput(attrs={'placeholder': 'Address'}),
                   'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'}),}