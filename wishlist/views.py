from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import AddToWishlistForm
from .models import Wishlist
from registerbook.models import Book
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def show_book_profile(request):
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            form.save()
            book_id = request.POST.get('book_id')
            book = Book.objects.get(id=book_id)
            preference = form.cleaned_data['preference']
            Wishlist.objects.create(user=request.user, book=book, preference=preference)
        return redirect('bookprofile')
    
    books = Book.objects.all()
    form = AddToWishlistForm()
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'bookprofile.html', context=context)

# @login_required
# def show_book_profile(request):
#     search_query = request.GET.get('search', '')  # Ambil parameter pencarian dari URL

#     if search_query:
#         # Jika ada parameter pencarian, lakukan pencarian buku
#         books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
#     else:
#         # Jika tidak ada parameter pencarian, tampilkan semua buku
#         books = Book.objects.all()

#     form = AddToWishlistForm()  # Formulir untuk menambahkan buku ke Wishlist

#     context = {
#         'books': books,
#         'form': form,
#         'search_query': search_query,  # Sertakan parameter pencarian dalam konteks
#     }

#     if request.method == 'POST':
#         form = AddToWishlistForm(request.POST)
#         if form.is_valid():
#             form.save()
#             book_id = request.POST.get('book_id')
#             book = Book.objects.get(id=book_id)
#             preference = form.cleaned_data['preference']
#             Wishlist.objects.create(user=request.user, book=book, preference=preference)
#             return redirect('bookprofile')

#     return render(request, 'bookprofile.html', context=context)


def show_book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

@login_required
def add_to_wishlist(request):
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['preference']
            preference = form.cleaned_data['preference']
            book = Book.objects.get(pk=book_id)
            Wishlist.objects.create(user=request.user, book=book, preference=preference)
            return redirect('wishlist:bookprofile')

    response_data = {'message': 'Terjadi kesalahan saat menambahkan buku ke Wishlist'}
    return JsonResponse(response_data, status=400)

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