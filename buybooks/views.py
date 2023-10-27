from django.shortcuts import render
from registerbook.models import Book

# Create your views here.
def show_test(request):
    context = {}
    return render(request, 'buybooks.html', context)

def show_book(request):
    book = Book.objects.all()

    context = {
        'book' : book
    }
    return render(request, 'buybooks.html')
