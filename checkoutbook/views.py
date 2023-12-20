import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from .models import CartItem, Checkout
from registerbook.models import Notification
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
import datetime
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt



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
        'currency' : 'SAR',
    }
    return render(request, 'checkout.html', context)

def show_checkout_json(request, username):
    # print("a")
    cart_items = CartItem.objects.filter(user__username = username, is_ordered=True)
    cart_data = [
        {
            'id': item.id,
            'title': item.book.title,
            'quantity': item.quantity,
            'subtotal': item.subtotal(),
            'currency': item.book.currency,
            'is_ordered' : item.is_ordered,
        }
        for item in cart_items
    ]

    return JsonResponse(cart_data, safe=False)

def get_total_harga(request, username):
    cart_items = CartItem.objects.filter(user__username = username, is_ordered=True)
    total_price = sum(item.subtotal() for item in cart_items)
    context = [{
        'total_harga' : total_price,
    }]
    return JsonResponse(context, safe=False)


@csrf_exempt
def checkout_ajax(request):
    try:
        if request.method == 'POST':
            user = request.user
            items = CartItem.objects.filter(user=request.user, is_ordered=True)
            alamat = request.POST.get("alamat")
            metode_pembayaran = request.POST.get("metode_pembayaran")

            total_price = sum(item.subtotal() for item in items)
            new_item = Checkout(
                            user=user, 
                            alamat=alamat, 
                            metode_pembayaran=metode_pembayaran, 
                            total_price=total_price
                        )
            
            new_item.save()
            new_item.items.set(items)
            new_item.save()
            
            message = f"Pesanan masuk dari {user.username}.\n"
            message += f"{new_item.alamat} | {new_item.metode_pembayaran} | SAR {new_item.total_price}\n"
            message += "\nOrder Summary:\n"
            for item in items:
                message += f"- {item.book.title}\n"
                
            Notification.objects.create(buyer=user, message=message)
            for item in items:
                item.delete()

            return HttpResponseRedirect(reverse('buybooks:show_cart'))
        
        return HttpResponseNotFound()
    except: 
        return JsonResponse({"user" : user, 
                             "items" : items, 
                             "alamat" : alamat, 
                             "metode_pembayaran" : metode_pembayaran,
                             "total_price" : total_price,
                             "new_item" : new_item})

@login_required
@csrf_exempt
def checkout_flutter(request):
    if request.method == 'POST':
        user = request.user
        items = CartItem.objects.filter(user=request.user, is_ordered=True)

        data = json.loads(request.body)
        alamat = data["alamat"]
        metode_pembayaran = data["metode_pembayaran"]
        total_price = int(data["total_harga"])
        new_item = Checkout(
                        user=user, 
                        alamat=alamat, 
                        metode_pembayaran=metode_pembayaran, 
                        total_price=total_price
                    )
        
        new_item.save()
        new_item.items.set(items)
        new_item.save()
        
        message = f"Pesanan masuk dari {user.username}.\n"
        message += f"{new_item.alamat} | {new_item.metode_pembayaran} | SAR {new_item.total_price}\n"
        message += "\nOrder Summary:\n"
        for item in items:
            message += f"- {item.book.title}\n"
            
        Notification.objects.create(buyer=user, message=message)
        for item in items:
            item.delete()
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
def show_myorder(request):
    orders = Checkout.objects.filter(user = request.user)
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

def get_order_json_all(request):
    orders = Checkout.objects.all()
    order_data = [
        {
            'model' : "checkoutbook.checkout",
            'pk' : order.pk,
            'fields' : {
                'user': order.user.username,
                'alamat' : order.alamat,
                'metode_pembayaran': order.metode_pembayaran,
                'total_price' : order.total_price,
            }
        }
        for order in orders
    ]
    json_data = json.dumps(order_data)
    return HttpResponse(json_data, content_type="application/json")

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