from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('place_order', views.place_order, name='place_order'),
    path('product_details', views.product_details, name='product_details'),
    path('register', views.register, name="register"),
    path('search_result', views.search_result, name="search_result"),
    path('signin', views.signin, name="signin"),
    path('store', views.store, name="store"),
]
