from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Product, Category, Review
from cart.forms import CartQuantityForm


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
    cart = CartQuantityForm()
    reviews = Review.objects.filter(product=product).all()[:3]
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            return redirect(product.get_absolute_url())
    else:
        form = ReviewForm()
    return render(request, 'home/detail_product.html', {'product': product, 'reviews': reviews,
                                                        'form': form, 'cart': cart})
