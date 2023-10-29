import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseNotFound
# Create your views here.
@login_required(login_url='/login')
def show_buybooks(request):
    books = Book.objects.all()
    form = AddToCart()

    context = {
        'books': books,
        'form' : form,
    }
    
    return render(request, 'buybooks.html', context)

def add_cart_ajax(request, id):
    if request.method == 'POST':
        user = request.user
        book = Book.objects.get(pk=id)
        quantity = request.POST.get("quantity")
        is_ordered = False  
        new_item = CartItem(user=user, book=book, quantity=quantity, is_ordered=is_ordered)
        new_item.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/login')
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cartwindow.html', context)

def delete_cart(request, id):
    item = get_object_or_404(CartItem, pk=id)
    if request.method == 'POST':
        item.delete()
    return redirect('buybooks:show_cart')

def show_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_books_json_rating_lt(request):
    books = Book.objects.filter(rating__lt=4)
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_books_json_rating_gte(request):
    books = Book.objects.filter(rating__gte=4)
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def selected(request, id):
    item = CartItem.objects.get(pk=id)
    item.is_ordered = True
    item.save()
    return redirect('buybooks:show_cart')