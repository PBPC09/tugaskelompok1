import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Book, CartItem
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
@login_required
def show_buybooks(request):
    books = Book.objects.all()
    form = AddToWishlistForm()

    context = {
        'books': books,
        'form' : form,
    }
    return render(request, 'buybooks.html', context)

def add_cart_ajax(request):
    if request.method == 'POST':
        # book = request.POST.get("book")
        # price = request.POST.get("price")
        return

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