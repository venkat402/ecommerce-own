from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from product.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def get_categories(request, slug):
    products = Product.objects.select_related('category').filter(category__slug=slug)
    p = Paginator(products, 3)

    page_number = request.GET.get('page')
    try:
        p_obj = p.page(page_number)
    except PageNotAnInteger:
        p_obj = p.page(1)
    except EmptyPage:
        p_obj = p.page(p.num_pages)
    context = {
        "products": p_obj,
        "count": p.count
    }
    return render(request, 'category-products.html', context)
