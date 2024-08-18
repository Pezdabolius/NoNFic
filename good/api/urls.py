from django.urls import path
from . import views


urlpatterns = [
    path('category/<pk>/', views.CategoryDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('review/', views.ReviewList.as_view()),
    path('product/<pk>/', views.ProductDetailView.as_view())
]