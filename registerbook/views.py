from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import Book, Notification
from checkoutbook.models import Checkout

@login_required(login_url='/login')
def show_registered_books(request):
    books = Book.objects.all()
   
    context = {
        'username': request.user,
        'books': books,
    }

    return render(request, 'regist_book.html', context=context)

@login_required(login_url='/login')
def show_received_orders(request):
    notifications = Notification.objects.all().order_by('-timestamp')

    context = {
        'username': request.user,
        'notifications': notifications,
    }

    return render(request, 'received_orders.html', context=context)

def show_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    rating_filter = request.GET.get('rating_filter')
    
    if rating_filter == "gt4":
        books = Book.objects.filter(rating__gt=4)
    elif rating_filter == "lte4":
        books = Book.objects.filter(rating__lte=4)
    else:
        books = Book.objects.all()
        
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
        user = request.user

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
            user=user
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_book(request, book_id):
    if request.method == "DELETE":
        book = Book.objects.get(pk=book_id)
        book.delete()
        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()

def mark_notification_read(request, notif_id):
    notif = Notification.objects.get(pk=notif_id)
    notif.is_read = True
    notif.save()
    # Anda dapat mengarahkan kembali ke halaman yang sama atau ke halaman ringkasan pesanan
    return redirect('registerbook:show_received_orders')

from django.http import JsonResponse

def get_order_details(request):
    notif_id = request.GET.get('notifId')
    notif = Notification.objects.get(pk=notif_id)
    order = Checkout.objects.filter(user=notif.buyer)

    data = {
        'alamat': order.alamat,
        'total_price': order.total_price
    }
    return JsonResponse(data)