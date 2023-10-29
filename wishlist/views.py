from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddToWishlistForm
from .models import Wishlist
from registerbook.models import Book
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 


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
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'bookprofile.html', context=context)

def show_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

@login_required
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

@login_required
def mywishlist(request):
    wishlist_books = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_books': wishlist_books
    }
    return render(request, 'mywishlist.html', context=context)

@login_required
def delete_wishlist_item(request, item_id):
    item = get_object_or_404(Wishlist, pk=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('wishlist:mywishlist')

def get_books(request):
    rating = request.GET.get('rating')

    books = Book.objects.all()
    if rating:
        books = books.filter(rating=rating)

    return render(request, 'books.html', {'books': books})