import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseNotFound

# Create your views here.
from django.db.models import Q
from django.shortcuts import render
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def show_buybooks(request):
    books = Book.objects.all()
    books, filters = apply_filters(request, books)
    context = {
        'books': books,
        'filters': filters,
    }
    return render(request, 'buybooks.html', context)

@login_required
def apply_filters(request, queryset):
    filters = {}
    
    rating = request.GET.get('rating')
    if rating:
        if float(rating) >= 0:
            queryset = queryset.filter(rating__gt=rating)
            filters['rating'] = rating
        else:
            queryset = queryset.filter(rating__lt=-float(rating))
            filters['rating'] = '-' + rating

    page_count = request.GET.get('page_count')
    if page_count:
        if int(page_count) >= 0:
            queryset = queryset.filter(page_count__gt=page_count)
            filters['page_count'] = page_count
        else:
            queryset = queryset.filter(page_count__lt=-int(page_count))
            filters['page_count'] = '-' + page_count

    price = request.GET.get('price')
    if price:
        if float(price) >= 0:
            queryset = queryset.filter(price__gt=price)
            filters['price'] = price
        else:
            queryset = queryset.filter(price__lt=-float(price))
            filters['price'] = '-' + price

    return queryset, filters

@login_required
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, book_id):
    # Logika penambahan buku ke keranjang di sini
    # Pastikan untuk menangani request POST dengan AJAX
    return JsonResponse({'message': 'Book added to cart.'})

@login_required
def remove_from_cart(request, cart_item_id):
    # Logika penghapusan buku dari keranjang di sini
    # Pastikan untuk menangani request POST dengan AJAX
    return JsonResponse({'message': 'Book removed from cart.'})




def add_cart_ajax(request, id):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        user = request.user
        book = Book.objects.get(pk=data["id"])
        quantity = request.POST.get("amount")
        is_ordered = False  
        new_item = CartItem(user=user, book=book, quantity=quantity, is_ordered=is_ordered)
        new_item.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'buybooks.html', context)

def get_cart_json(request):
    items = CartItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

def delete_cart_ajax(request, id):
    data = json.loads(request.body.decode("utf-8"))
    item = CartItem.objects.get(pk=data["id"])
    item.delete()
    return HttpResponse("DELETED",status=200)