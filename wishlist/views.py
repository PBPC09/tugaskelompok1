import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddToWishlistForm
from .models import Wishlist
from registerbook.models import Book
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages 
import datetime
from datetime import datetime

@login_required
def show_book_profile(request):
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)

        if form.is_valid():
            book_id = request.POST.get('book_id')
            book = get_object_or_404(Book, id=book_id)
            preference = form.cleaned_data['preference']
            Wishlist.objects.create(user=request.user, book=book, preference=preference)
        return redirect('bookprofile')
    
    rating = request.GET.get('rating')
    if rating and rating != ''and rating != 'All Ratings':
        lower_bound = float(rating)
        upper_bound = lower_bound + 0.9
        books = Book.objects.filter(rating__range=(lower_bound, upper_bound))
    else:
        books = Book.objects.all()
    
    form = AddToWishlistForm()
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'books': books,
        'form': form,
        'last_login' : formatted_without_ms,

    }
    return render(request, 'bookprofile.html', context=context)

def show_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')

    return render(request, 'book_details.html', {'book': book, 'last_login' : formatted_without_ms})

@login_required(login_url='/login')
@csrf_exempt
def add_to_wishlist(request):
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            book_id = request.POST.get('book_id')
            preference = form.cleaned_data['preference']
            book = Book.objects.get(pk=book_id)

            if Wishlist.objects.filter(user=request.user, book=book).exists():
                return JsonResponse({'status': 'error', 'message': f"Buku berjudul {book.title} sudah ada dalam wishlist Anda."})
            else:
                Wishlist.objects.create(user=request.user, book=book, preference=preference)
                return JsonResponse({'status': 'success', 'message': 'Book added to wishlist successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form is not valid.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

def mywishlist(request):
    wishlist_books = Wishlist.objects.filter(user=request.user)
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'wishlist_books': wishlist_books,
        'last_login' : formatted_without_ms,

    }

    return render(request, 'mywishlist.html', context=context)

@csrf_exempt
def delete_wishlist_item(request, item_id):
    item = get_object_or_404(Wishlist, pk=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('wishlist:mywishlist')

def get_books(request):
    rating = request.GET.get('rating')
    last_login = request.COOKIES['last_login']
    parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
    formatted_without_ms = parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')

    books = Book.objects.all()
    if rating:
        books = books.filter(rating=rating)

    return render(request, 'books.html', {'books': books, 'last_login' : formatted_without_ms})

def mywishlist_json(request):
    wishlist_books = Wishlist.objects.all()
    wishlist_data = [
        {
            'model' : "wishlist.wishlist",
            'pk' : wishlist.pk,
            'fields' : {
                'user': wishlist.user.username,
                'title': wishlist.book.title,
                'book_id' : wishlist.book.pk,
                'preference': wishlist.get_preference_display(),
            }
        }
        for wishlist in wishlist_books
    ]

    json_data = json.dumps(wishlist_data)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
# @require_http_methods(["POST"])
def add_to_wishlist_flutter(request):
    data = json.loads(request.body)
    username = data["username"]
    book_id = data["book_id"]
    preference = int(data["preference"])

    book = Book.objects.get(pk=book_id)
    user = User.objects.get(username=username)
    
    # TEST DOANG
    # return JsonResponse({'status': 'success', 'message': 'Book already in wishlist'}, status=200)

    if Wishlist.objects.filter(user=user, book=book).exists():
        return JsonResponse({'status': 'error', 'message': 'Book already in wishlist'}, status=400)

    Wishlist.objects.create(user=user, book=book, preference=preference)
    return JsonResponse({'status': 'success', 'message': 'Book added to wishlist successfully'}, status=200)

@csrf_exempt
def delete_wishlist_item_flutter(request, item_id):
    # print(item_id)
    if request.method == 'POST' :
        Wishlist.objects.get(pk=item_id).delete()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'failed'}, status=300)

def preference_level(level):
    if level == 1:
        return 'Not Interested'
    elif level == 2:
        return 'Maybe Later'
    elif level == 3:
        return 'Interested'
    elif level == 4:
        return 'Really Want It'
    elif level == 5:
        return 'Must Have'
    else:
        return 'Not Interested'
