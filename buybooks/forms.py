from django import forms
from buybooks.models import *
class AddToCart(forms.Form):
    class Meta:
        model = CartItem
        fields = ["quantity",]
