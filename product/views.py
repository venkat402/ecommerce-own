from django.shortcuts import render
from .models import Product
from reviews.models import Review


# Create your views here.


def product_details(request, slug):
    product = None
    reviews = None
    try:
        product = Product.objects.get(slug=slug)
        reviews = Review.objects.select_related('user').select_related(
            'product').select_related('user__profile').filter(product__id=product.id)
    except Exception:
        pass
    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'product-detail.html', context)
