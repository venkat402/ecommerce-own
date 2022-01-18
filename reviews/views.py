from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.contrib.auth.models import User
from product.models import Product
from django.contrib import messages


# Create your views here.


def submit_review(request):
    if request.method == "POST":
        try:
            product_id = request.POST.get('product_id')
            review = ReviewForm(request.POST)
            if review.is_valid():
                r = review.save(commit=False)
                r.user_id = request.user.id
                r.product = Product.objects.get(id=product_id)
                r.status = 1
                r.save()
                messages.info(request, "Review submitted successfully.")
            return redirect(request.META.get('HTTP_REFERER'))
        except Exception:
            messages.info(request, "Unable to submit the request")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))
