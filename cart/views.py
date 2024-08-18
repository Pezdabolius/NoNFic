from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from good.models import Product
from django.shortcuts import render
from .forms import CartQuantityForm, OrderForm
from .models import CartOrder
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


def order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                CartOrder.objects.create(
                    order=order, product=item['product'],
                    price=item['price'], quantity=item['quantity']
                )
                product = item['product']
                product.count_sold += item['quantity']
                product.save()
            cart.clear()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'order/checkout.html', {'form': form, 'cart': cart})