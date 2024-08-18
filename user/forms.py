from django import forms
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    rep_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))
    conditions = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email', 'required': True})}

    def clean(self):
        cd = self.cleaned_data
        if cd['password'] != cd['rep_password'] or len(cd['password']) < 8:
            raise ValidationError('Passwords do not match')
        elif User.objects.filter(username=cd['username']).exists():
            raise ValidationError('Username is taken')
        elif User.objects.filter(email=cd['email']).exists():
            raise ValidationError('Email is taken')
        return cd


