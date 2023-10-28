from django import forms
from .models import Checkout

class CheckoutForm(forms.Form):
    class Meta:
        model = Checkout
        fields = ["alamat", "metode_pembayaran"]