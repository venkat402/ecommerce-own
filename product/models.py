from django.db import models
from category.models import Category


# Create your models here.


class Product(models.Model):
    colors = (
        ('R', 'Red'),
        ('G', 'Green'),
        ('W', 'While'),
        ('B', 'Black'),
        ('P', 'Pink'),
    )

    size = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('X', 'Extra Large'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    sku = models.CharField(max_length=25)
    price = models.FloatField(default=None)
    color = models.CharField(max_length=1, choices=colors)
    size = models.CharField(max_length=1, choices=size)
    images = models.ImageField(upload_to='product_images', default=None)
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    weight = models.FloatField(default=None)
    description = models.TextField(default=None)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.name
