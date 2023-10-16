from django.views.generic import ListView, DetailView

from book.models import *


# Create your views here.


class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name = 'books.html'


class BookDetailView(DetailView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = 'book'
    template_name = 'book_detail.html'
