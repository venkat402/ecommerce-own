from django.shortcuts import render, redirect
from .forms import CartForm
from .models import Cart, CartItem
from django.contrib import messages


# Create your views here.


def add_to_cart(request):
    if request.method == 'POST':
        cart = check_active_cart(request)

        data = request.POST
        cart_form = CartForm(data)
        if cart_form.is_valid():
            citem = CartItem()
            citem.quantity = 1
            citem.cart = cart
            citem.product_id = request.POST.get('product_id')
            citem.save()
            return redirect('get_cart')
        else:
            context = {'form': cart_form}
            return render(request, 'cart.html', context)
    else:
        return redirect('get_cart')


def check_active_cart(request):
    user_id = request.user.id
    cart = Cart.objects.filter(status=True, user=user_id)[0]
    if cart:
        return cart
    else:
        return create_cart(request)


def create_cart(request):
    cart = Cart()
    cart.user_id = request.user.id
    cart.status = 1
    cart.save()
    return cart


def get_cart(request):
    user_id = request.user.id
    items = CartItem.objects.select_related('cart').select_related('product').filter(cart__user=user_id, cart__status=1)

    total = 0
    for i in items:
        item_total = i.quantity * i.product.price
        total += item_total

    tax = 0
    grand_total = total + tax
    context = {'items': items, "total": total, "tax": tax, "grand_total": grand_total}
    return render(request, 'cart.html', context)


def update_cart(request):
    cart_id = request.POST.get('cart_id')
    quantity = int(request.POST.get('quantity'))
    if quantity > 0:
        cart = CartItem.objects.get(id=cart_id)
        cart.quantity = quantity
        cart.save()
        messages.info(request, "Cart item updated successfully")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.info(request, "Invalid quantiy")
        return redirect(request.META.get('HTTP_REFERER'))


def delete_cart_item(request, pk):
    cartitem = CartItem.objects.filter(pk=pk)
    try:
        cartitem.delete()
    except Exception:
        pass
    return redirect('get_cart')


def checkout(request):
    user_id = request.user.id
    items = CartItem.objects.select_related('cart').select_related('product').filter(cart__user=user_id, cart__status=1)

    total = 0
    for i in items:
        item_total = i.quantity * i.product.price
        total += item_total

    tax = 0
    grand_total = total + tax
    context = {'items': items, "total": total, "tax": tax, "grand_total": grand_total}
    return render(request, 'place-order.html', context)
