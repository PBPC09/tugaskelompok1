from django.shortcuts import render, redirect
from registerbook.models import Book
from .models import Buybooks

# Create your views here.
def show_test(request):
    context = {}
    return render(request, 'buybooks.html', context)

def show_book(request):
    book = Book.objects.all()

    context = {
        'book' : book
    }
    return render(request, 'buybooks.html', context=context)

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)

    # Cek apakah buku sudah ada di keranjang
    if Buybooks.objects.filter(book=book, user=request.user, is_ordered=False).exists():
        # Jika sudah ada, tambahkan jumlahnya
        cart_item = Buybooks.objects.get(book=book, user=request.user, is_ordered=False)
        cart_item.quantity += 1
        cart_item.save()
    else:
        # Jika belum ada, buat item baru di keranjang
        cart_item = Buybooks(user=request.user, book=book, quantity=1)
        cart_item.save()

    return redirect('show_books')

# Fungsi untuk menampilkan buku berdasarkan filter
def filter_books(request, price=None, rating=None, page_count=None):
    books = Book.objects.all()

    if price is not None:
        if price < 30:
            books = books.filter(price__lt=30)
        elif price >= 30:
            books = books.filter(price__gte=30)
    
    if rating is not None:
        if rating < 3:
            books = books.filter(rating__lt=3)
        elif rating >= 3:
            books = books.filter(rating__gte=3)
    
    if page_count is not None:
        if page_count < 100:
            books = books.filter(page_count__lt=100)
        elif page_count >= 100:
            books = books.filter(page_count__gte=100)

    context = {
        'books': books
    }
    return render(request, 'buybooks.html', context)
