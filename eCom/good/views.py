from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator


def best_selling(request):
    products = Product.objects.filter(available=True)
    return render(request, 'home/home.html',
                  {products: 'products'})


def products_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # paginator = Paginator(products, 3)
    # page_number = request.GET.get('page', 1)
    # products = paginator.page(page_number)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'home/list.html',
           {'category': category,
            'categories': categories,
            'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug, available=True)
    return render(request, 'home/goods/detail.html',
           {'product': product})