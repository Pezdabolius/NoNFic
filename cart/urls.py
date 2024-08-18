from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart'),
    path('checkout/', views.order, name='checkout'),
    path('add/<slug:slug>/', views.add_cart, name='add_cart'),
    path('remove/<slug:slug>/', views.remove_cart, name='remove_cart'),
    path('delete/<slug:slug>', views.delete_cart, name='delete_cart'),
]