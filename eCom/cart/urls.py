from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart'),
    path('add/<slug:slug>/', views.add_cart, name='add_cart'),
    path('remove/<slug:slug>', views.remove_cart, name='remove_cart'),
]