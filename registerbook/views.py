from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import Book, Profile, Order

@login_required(login_url='/login')
def show_registered_books(request):
    books = Book.objects.filter(seller__user=request.user)
   
    context = {
        'username': request.user,
        'books': books,
    }

    return render(request, 'regist_book.html', context=context)

@login_required(login_url='/login')
def show_received_orders(request):
    received_orders = Order.objects.filter(seller__user=request.user)
    context = {
        'username': request.user,
        'orders': received_orders,
    }

    return render(request, 'received_orders.html', context=context)

def show_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    books = Book.objects.filter(seller__user=request.user)
    return HttpResponse(serializers.serialize('json', books))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.POST.get("author")
        rating = float(request.POST.get("rating"))
        voters = int(request.POST.get("voters"))
        price = float(request.POST.get("price"))
        currency = request.POST.get("currency")
        description = request.POST.get("description")
        publisher = request.POST.get("publisher")
        page_count = int(request.POST.get("page_count"))
        genres = request.POST.get("genres")
        seller_profile = Profile.objects.get(user=request.user)

        new_book = Book(
            title=title, 
            author=author, 
            rating=rating,
            voters=voters, 
            price=price, 
            currency=currency,
            description=description, 
            publisher=publisher,
            page_count=page_count, 
            genres=genres, 
            seller=seller_profile
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
    
@csrf_exempt
def remove_book(request, book_id):
    if request.method == "DELETE":
        book = Book.objects.get(pk=book_id, seller__user=request.user)
        book.delete()
        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()