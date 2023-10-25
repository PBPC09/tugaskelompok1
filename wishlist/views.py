from django.shortcuts import render, redirect
from .models import Book, Wishlist
from .forms import AddToWishlistForm 

def BookProfile(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            Wishlist.objects.create(
                user=request.user,
                book=book,
                preference=form.cleaned_data['preference']
            )
            return redirect('wishlist_page')
    else:
        form = AddToWishlistForm()
    return render(request, 'book_profile.html', {'book': book, 'form': form})

def WishlistPage(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})
