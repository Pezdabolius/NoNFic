from django import forms


class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=[str(i) for i in range(1,11)],
        coerce=int,
    )
    update = forms.BooleanField(initial=False, required=False)