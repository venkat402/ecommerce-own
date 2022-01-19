from django.urls import path, include
from . import views

urlpatterns = [
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('get_cart', views.get_cart, name="get_cart"),
    path('delete_cart_item/<pk>', views.delete_cart_item, name="delete_cart_item"),
    path('update_cart', views.update_cart, name="update_cart"),
    path('checkout', views.checkout, name="checkout"),
]
