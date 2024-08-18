from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartList.as_view()),
]