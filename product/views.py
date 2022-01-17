from django.shortcuts import render
from .models import Product


# Create your views here.


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product-detail.html', context)
