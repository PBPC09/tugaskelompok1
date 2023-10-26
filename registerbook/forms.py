from django.forms import ModelForm
from registerbook.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "rating", 
                  "voters", "price", "currency", 
                  "publisher", "page_count", 
                  "genres", "description"]