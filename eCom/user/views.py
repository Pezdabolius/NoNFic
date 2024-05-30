from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('home')
        else:
            return redirect('registration')
    else:
        form = RegistrationForm()
    return render(request, 'account/sign_up.html', {'form': form})
