from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Product, Review
from cart.forms import CartQuantityForm
from django.core.cache import cache


def best_selling(request):
    products = Product.objects.filter(available=True).order_by('-count_sold')[:6]
    return render(request, 'home/home.html',
                  {'products': products})


def products_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'home/list_products.html',
           {'products': products})


def product_detail(request, slug):
    context = cache.get(f"product_detail_{slug}")
    if context is None:
        product = get_object_or_404(Product, slug=slug, available=True)
        sim_products = Product.objects.filter(category=product.category).exclude(id=product.id)
        reviews = Review.objects.filter(product=product).all()[:3]

        context = {
            'product': product,
            'sim_products': sim_products,
            'reviews': reviews,
        }
        cache.set(f"product_detail_{slug}", context, timeout=900)
    cart = CartQuantityForm()
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            product.count_reviews += 1
            product.save()
            review.save()
            return redirect(product.get_absolute_url())
    else:
        form = ReviewForm()
    return render(request, 'home/detail_product.html',
                  {**context, 'form': form, 'cart': cart})
