from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import AddToWishlistForm
from .models import Book, Wishlist
from django.http import JsonResponse

def bookprofile(request, book_id):
=======
from .models import Book, Wishlist
from .forms import AddToWishlistForm 

def BookProfile(request, book_id):
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
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

=======
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
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
