import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseNotFound
# Create your views here.
@login_required
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
    return render(request, 'cartwindow.html', context)

def get_cart_json(request):
    items = CartItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

def delete_cart_ajax(request, id):
    data = json.loads(request.body.decode("utf-8"))
    item = CartItem.objects.get(pk=data["id"])
    item.delete()
    return HttpResponse("DELETED",status=200)

def show_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")