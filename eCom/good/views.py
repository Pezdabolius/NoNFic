from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def best_selling(request):
    products = Product.objects.filter(available=True)[:6]
    return render(request, 'home/home.html',
                  {'products': products})


def products_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'home/list_products.html',
           {'category': category,
            'categories': categories,
            'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'home/detail_product.html',
           {'product': product})