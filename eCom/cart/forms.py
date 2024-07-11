from django import forms


class CartAddForm(forms.Form):
    update = forms.BooleanField(initial=False, required=False,
                                widget=forms.HiddenInput)