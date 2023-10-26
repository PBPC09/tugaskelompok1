from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Book
from .forms import BookForm

def show_registered_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registerbook:show_registered_books')
    
    books = Book.objects.all()
    form = BookForm()
    context = {
        'books': books,
        'form': form,
    }

    return render(request, 'registbook.html', context=context)

def regist_books(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")