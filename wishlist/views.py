from django.shortcuts import render, redirect
from .forms import AddToWishlistForm
from .models import Book, Wishlist
from django.http import JsonResponse

def bookprofile(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            preference = form.cleaned_data['preference']
            Wishlist.objects.create(user=request.user, book=book, preference=preference)
            return redirect('wishlist_page')
    else:
        form = AddToWishlistForm()
    return render(request, 'bookprofile.html', {'form': form})

# def bookprofile(request):
#     form = AddToWishlistForm()
#     return render(request, 'bookprofile.html', {'form': form})

def wishlistpage(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def addtowishlist(request, book_id):
    if request.method == "POST":
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            preference = form.cleaned_data['preference']
            Wishlist.objects.create(user=request.user, book_id=book_id, preference=preference)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})