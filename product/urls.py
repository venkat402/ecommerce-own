from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/', views.product_details, name='product_detail')
]
