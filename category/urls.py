from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug>', views.get_categories, name="get_categories"),
]
