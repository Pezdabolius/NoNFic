from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('sign_up/', views.registration_user, name='registration')
]