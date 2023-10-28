from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.http import JsonResponse
from .models import CartItem, Checkout
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required

@login_required
def show_checkout(request):
    form = CheckoutForm()
    cart_items = CartItem.objects.filter(user=request.user, is_ordered=True)
    total_price = sum(item.subtotal() for item in cart_items)
    context = {
        'cart_items': cart_items, 
        'total_price': total_price,
        'form': form,
    }
    return render(request, 'checkout.html', context)
    
@login_required
def checkout_ajax(request):
    if request.method == 'POST':
        user = request.user
        items = CartItem.objects.filter(user=request.user, is_ordered=True)
        alamat = request.POST.get("alamat")
        metode_pembayaran = request.POST.get("metode_pembayaran")

        new_item = Checkout(user=user, items=items, alamat=alamat, metode_pembayaran=metode_pembayaran)
        new_item.save()

        for item in items:
            item.delete()

        return HttpResponseRedirect(reverse('buybooks:show_cart'))

    return HttpResponseNotFound()