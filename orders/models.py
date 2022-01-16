from django.db import models
from cart.models import Cart
from payment.models import Payment
from django.contrib.auth.models import User


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey('payment.Payment', on_delete=models.SET_NULL, related_name='+', null=True)
    billing_address = models.TextField(default='')
    shipping_address = models.TextField(default='')
    mobile = models.CharField(max_length=20, default='')
    tracking = models.CharField(max_length=255, default='')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
