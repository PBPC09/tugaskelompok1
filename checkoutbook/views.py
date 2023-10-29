import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.core import serializers
from .models import CartItem, Checkout
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
import datetime
from datetime import datetime
@login_required(login_url='/login')
def show_checkout(request):
    form = CheckoutForm()
    cart_items = CartItem.objects.filter(user=request.user, is_ordered=True)
    total_price = sum(item.subtotal() for item in cart_items)
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'cart_items': cart_items, 
        'total_price': total_price,
        'last_login' : formatted_without_ms,
        'form': form,
        'currency' : cart_items[0].book.currency,
    }
    return render(request, 'checkout.html', context)
    
def checkout_ajax(request):
    if request.method == 'POST':
        user = request.user
        items = CartItem.objects.filter(user=request.user, is_ordered=True)
        alamat = request.POST.get("alamat")
        metode_pembayaran = request.POST.get("metode_pembayaran")
        total_price = sum(item.subtotal() for item in items)

        new_item = Checkout(user=user, alamat=alamat, metode_pembayaran=metode_pembayaran, total_price=total_price)
        new_item.save()

        new_item.items.set(items)
        new_item.save()

        for item in items:
            item.delete()

        return HttpResponseRedirect(reverse('buybooks:show_cart'))

    return HttpResponseNotFound()

@login_required(login_url='/login')
def show_myorder(request):
    orders = Checkout.objects.all()
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'orders': orders,
        'last_login' : formatted_without_ms,

    }
    return render(request, 'myorder.html', context)

def get_order_json(request):
    orders = Checkout.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', orders))

def get_order_json_cc(request):
    orders = Checkout.objects.filter(user=request.user, metode_pembayaran="kartu_kredit")
    return HttpResponse(serializers.serialize('json', orders), content_type="application/json")

def get_order_json_dc(request):
    orders = Checkout.objects.filter(user=request.user, metode_pembayaran="kartu_debit")
    return HttpResponse(serializers.serialize('json', orders), content_type="application/json")

def get_order_json_tf(request):
    orders = Checkout.objects.filter(user=request.user, metode_pembayaran="transfer_bank")
    return HttpResponse(serializers.serialize('json', orders), content_type="application/json")

def get_order_json_ew(request):
    orders = Checkout.objects.filter(user=request.user, metode_pembayaran="e_wallet")
    return HttpResponse(serializers.serialize('json', orders), content_type="application/json")