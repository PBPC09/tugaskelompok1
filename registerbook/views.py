from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from .models import Book
from .forms import BookForm

def show_registered_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'regist_book.html', context=context)

def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('registerbook:show_registered_books'))

    context = {'form': form}
    return render(request, "add_book.html", context)

def regist_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")