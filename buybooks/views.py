import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from .forms import AddToCart
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_buybooks(request):
    books = Book.objects.all()
    form = AddToCart()
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'books': books,
        'form' : form,
        "last_login":formatted_without_ms,
    }
    
    return render(request, 'buybooks.html', context)

@login_required(login_url='/login')
@csrf_exempt
def add_cart_ajax(request, id):
    if request.method == 'POST':
        user = request.user
        book = Book.objects.get(pk=id)
        quantity = request.POST.get("quantity")
        is_ordered = False  

        new_item = CartItem(
            user=user, 
            book=book, 
            quantity=quantity, 
            is_ordered=is_ordered
        )
        new_item.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@login_required(login_url='/login')
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_data = [
        {
            'id': item.id,
            'title': item.book.title,
            'quantity': item.quantity,
            'subtotal': item.subtotal(),
            'currency': item.book.currency
        }
        for item in cart_items
    ]

    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
    
    context = {
        'cart_data': cart_data,
        'last_login' : formatted_without_ms,
    }
    
    return render(request, 'cartwindow.html', context)

@csrf_exempt
def delete_cart(request, id):
    item = get_object_or_404(CartItem, pk=id)
    if request.method == 'POST':
        item.delete()
    return redirect('buybooks:show_cart')

@csrf_exempt
def delete_cart_flutter(request, id):
    if request.method == 'POST' :
        CartItem.objects.get(pk=id).delete()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'failed'}, status=300)

def show_books_json(request):
    rating_gte = request.GET.get('rating_gte')
    rating_lt = request.GET.get('rating_lt')

    if rating_gte:
        books = Book.objects.filter(rating__gte=rating_gte)
    elif rating_lt:
        books = Book.objects.filter(rating__lt=rating_lt)
    else:
        books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_books_json_rating_lt(request):
    books = Book.objects.filter(rating__lt=4)
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_books_json_rating_gte(request):
    books = Book.objects.filter(rating__gte=4)
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

@csrf_exempt
def selected(request, id):
    item = CartItem.objects.get(pk=id)
    if item.is_ordered == False :
        item.is_ordered = True
    else:
        item.is_ordered = False  
    item.save()

    return redirect('buybooks:show_cart')

@csrf_exempt
def selected_flutter(request, id):
    if request.method == 'POST':
        item = CartItem.objects.get(pk=id)
        if item.is_ordered == False :
            item.is_ordered = True
        else:
            item.is_ordered = False  
        item.save()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'failed'}, status=300)


# def show_cart_json(request, uname):
#     data_item = CartItem.objects.all()
#     for data in data_item:
#         if data.user.username == uname:
#             user_id = data.user
#             data = CartItem.objects.filter(user = user_id)
#             break
#         else:
#             data = []
#     return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_cart_json(request, uname):
    user = get_object_or_404(User, username=uname)
    cart_items = CartItem.objects.filter(user=user)

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

def show_carts_json(request):
    books = CartItem.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

@login_required
@csrf_exempt
def add_to_cart(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=id)
        new_cart = CartItem.objects.create(
            user = request.user,
            book = book,
            quantity = data["quantity"],
            is_ordered = False
        )
        new_cart.save()
        return JsonResponse({'status': 'success', 'message': 'Book added to wishlist successfully!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Form is not valid.'})