from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from product.models import Product


# Create your views here.


def get_categories(request, slug):
    products = Product.objects.select_related('category').filter(category__slug=slug)
    context = {
        "products": products,
        "count": products.count()
    }
    return render(request, 'category-products.html', context)

