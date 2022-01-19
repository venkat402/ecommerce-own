from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='+')
    payment_type = models.CharField(max_length=100, default='')
    provider = models.CharField(max_length=100, default='')
    amount = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
