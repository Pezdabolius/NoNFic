from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('user/', views.get_user),
    path('signup/', views.sign_up),
]