from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.CartList.as_view()),
]