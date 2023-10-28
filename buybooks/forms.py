from django import forms
from buybooks.models import *
class AddToWishlistForm(forms.Form):
    class Meta:
        model = CartItem
        fields = ["quantity",]

class AddToCart(forms.Form):
    class Meta:
        model = CartItem
        fields = ["quantity",]

