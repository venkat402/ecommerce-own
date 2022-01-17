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
from .forms import RegistrationForm, UserProfileForm
from django.contrib.auth.hashers import make_password


# Create your views here.
def register(request):
    if request.method == "POST":
        data = dict(request.POST)
        data['password'] = make_password(data['password'][0])
        reg_form = RegistrationForm(data)
        pro_form = UserProfileForm(data)
        if reg_form.is_valid() and pro_form.is_valid():
            raise Exception(reg_form.password)
            user = reg_form.save()
            profile = pro_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "User account created successfully")
            return redirect('signin')
        else:
            context = {
                "form": reg_form,
                "form2": pro_form
            }
            return render(request, 'register.html', context)

    else:
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
    name = request.GET.get('name', '')
    sizes = request.GET.getlist('sizes[]', '')
    colors = request.GET.getlist('colors[]', '')
    min = request.GET.get('min', 0)
    max = request.GET.get('max', 10 ** 10)
    products = Product.objects.filter(
        Q(name__icontains=name) | Q(description__icontains=name) | Q(size__in=sizes) | Q(color__in=colors)).filter(
        price__range=(min, max))

    context = {
        "search": True,
        "products": products,
        "count": products.count()

    }
    return render(request, 'store.html', context)
