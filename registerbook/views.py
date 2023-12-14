import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from django.core import serializers
from main.models import Profile
from .models import Book
import datetime
from datetime import datetime
from .models import Notification

@login_required(login_url='/login')
def show_registered_books(request):
    books = Book.objects.all()
    
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'last_login' : formatted_without_ms,
        'username': request.user,
        'books': books,
    }

    return render(request, 'regist_book.html', context)

@login_required(login_url='/login')
def show_received_orders(request):
    last_login = request.COOKIES.get('last_login')
    if last_login:
        parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
        formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        formatted_without_ms = ""

    notifications = Notification.objects.all().order_by('-timestamp')

    context = {
        'username': request.user,
        'notifications': notifications,
        'last_login' : formatted_without_ms,
    }

    return render(request, 'received_orders.html', context)

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

def get_notif_json(request):
    notif = Notification.objects.all()
    return HttpResponse(serializers.serialize('json', notif))

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
        # user = request.user

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
            # user=user
        )
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
# @login_required(login_url='/login')
def create_book_flutter(request):
    if request.method == 'POST':  
        data = json.loads(request.body)

        new_book = Book.objects.create(
            title = data["title"],
            author = data["author"],
            rating = float(data["rating"]),
            voters = int(data["voters"]),
            price = float(data["price"]),
            currency = data["currency"],
            description = data["description"],
            publisher = data["publisher"],
            page_count = int(data["page_count"]),
            genres = data["genres"],
        )
        new_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def remove_book(request, book_id):
    if request.method == "DELETE":
        try:
            book = Book.objects.get(pk=book_id)
            book.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({"status": "failed", "error": "Book not found"}, status=404)
    return HttpResponseNotAllowed(['DELETE'])

@csrf_exempt
def mark_notification_read(request, notif_id):
    try:
        notif = Notification.objects.get(pk=notif_id)
        notif.is_read = True
        notif.save()
        return JsonResponse({"status": "success"}, status=200)
    except Notification.DoesNotExist:
        return JsonResponse({"status": "failed", "error": "Notification not found"}, status=404)

@csrf_exempt
def remove_notification(request, notif_id):
    if request.method == "DELETE":
        try:
            notif = Notification.objects.get(pk=notif_id)
            notif.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Notification.DoesNotExist:
            return JsonResponse({"status": "failed", "error": "Notification not found"}, status=404)
    return HttpResponseNotAllowed(['DELETE'])

@login_required(login_url='/login')
@csrf_exempt
def mark_all_notifications_read(request):
    user_profile = Profile.objects.get(user=request.user)
    Notification.objects.filter(buyer=user_profile).update(is_read=True)
    return JsonResponse({"status": "success"}, status=200)
