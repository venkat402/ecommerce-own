from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from category.models import Category
from product.models import Product
from configuration.models import Configuration
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    return render(request, "register.html")


def signin(request):
    username = None
    password = None
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                messages.success(request, "User login successfully.")
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "User account is not activated")
                return redirect('/signin')
        else:
            messages.warning(request, "Invalid credentials")

            return redirect('%s?next=%s' % ('/signin', request.path))
    else:
        return render(request, "signin.html")


def user_logout(request):
    logout(request)
    messages.info(request, "User successfully logout.")
    return redirect('/signin')


def home(request):
    products = Product.objects.all().order_by('?')[:8]
    context = {
        "products": products
    }
    return render(request, "index.html", context)


def cart(request):
    return render(request, "cart.html")


def dashboard(request):
    return render(request, "dashboard.html")


def place_order(request):
    return render(request, "place-order.html")


def product_details(request, slug):
    return render(request, "product-detail.html")


def get_store(request):
    products = Product.objects.all().order_by('-id')[:20]
    context = {
        "products": products,
        "count": products.count()
    }
    return render(request, 'store.html', context)


def search(request):
    name = request.GET['name']
    products = Product.objects.filter(Q(name__icontains=name) | Q(description__icontains=name))
    context = {
        "search": True,
        "products": products,
        "count": products.count()
    }
    return render(request, 'store.html', context)
