from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.best_selling, name='home'),
    path('shop/', views.products_list, name='products_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]