from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from good.models import Product
from django.shortcuts import render
from .forms import CartAddForm
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html',
                  {'cart': cart})


@require_POST
def add_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart')


@require_POST
def remove_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product=product)
    return redirect('cart')