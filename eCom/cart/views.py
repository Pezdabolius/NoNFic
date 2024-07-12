from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from good.models import Product
from django.shortcuts import render
from .forms import CartQuantityForm
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity'] = CartQuantityForm(initial={'update': True})
    return render(request, 'cart/detail.html',
                  {'cart': cart})


@require_POST
def add_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    form = CartQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, update_quantity=cd['update'])
    return redirect('cart')


@require_POST
def remove_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    form = CartQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product=product, update_quantity=cd['update'])
    return redirect('cart')


def delete_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.delete(product=product)
    return redirect('cart')