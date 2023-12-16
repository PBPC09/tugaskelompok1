from django import forms
from buybooks.models import CartItem
class AddToCart(forms.Form):
    class Meta:
        model = CartItem
        fields = ["quantity"]
