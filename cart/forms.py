from django import forms
from .models import Cart, CartItem


class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['color', 'size']
