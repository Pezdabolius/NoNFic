from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:slug>/', views.products_list, name='products_list_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]