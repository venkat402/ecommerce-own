from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('search/', views.search, name='search'),
    path('cart', views.cart, name='cart'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('register', views.register, name="register"),
    path('signin', views.signin, name="signin"),
    path('store', views.get_store, name="get_store"),
    path('logout', views.user_logout, name='user_logout')
]
