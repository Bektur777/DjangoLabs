from django.views.generic import ListView

from book.models import *


# Create your views here.


class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name = 'books/books.html'
