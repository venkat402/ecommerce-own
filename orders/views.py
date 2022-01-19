from django.shortcuts import render, redirect
from .models import Order
from payment.models import Payment
import json
from cart.models import Cart, CartItem

# Create your views here.


# you need to utilize payment and order table
# first will insert the data into ordre table
"""
if payment is success then order table status will be 1 
else order table status will be 0 
else payment id will be none 
after checking all conditions are ture then make cart table status as 0 
"""


def place_order(request):
    billing_address = dict()
    shipping_address = dict()
    for k, v in request.POST.items():
        if 'billing' in k:
            billing_address[k] = v
        if 'delivery' in k:
            shipping_address[k] = v
    grand_total = request.POST.get('grand_total')
    payment_option = request.POST.get('payment-option')
    user_id = request.user.id
    cart_id = Cart.objects.filter(status=True, user=user_id)[0]

    billing_address = json.dumps(billing_address)
    shipping_address = json.dumps(shipping_address)
    user_id = request.user.id
    order = Order()
    order.billing_address = billing_address
    order.shipping_address = shipping_address
    order.status = 0
    order.user = request.user
    order.cart = cart_id
    order.payment = None
    order.save()

    cart_id.status = 0
    cart_id.save()

    return redirect('index')


def store_billing(request):
    pass


def store_shipping(request):
    pass


# make payment and store in payment table
def make_payment(request):
    pass
