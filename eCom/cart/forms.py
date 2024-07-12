from django import forms


class CartQuantityForm(forms.Form):
    update = forms.BooleanField(initial=False, required=False,
                                widget=forms.HiddenInput)