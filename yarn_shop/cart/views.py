from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddYarnForm
from shop.models import Yarn


@require_POST
def cart_add(request, yarn_id):
    cart = Cart(request)
    yarn = get_object_or_404(Yarn, id=yarn_id)
    form = CartAddYarnForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(yarn=yarn,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, yarn_id):
    cart = Cart(request)
    yarn = get_object_or_404(Yarn, id=yarn_id)
    cart.remove(yarn)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddYarnForm(initial={'quantity': item['quantity'],
                                                                'update': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})


