from django.views.generic import *

from book.models import *
from book.forms import *


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


class ReviewBookListView(ListView):
    model = ReviewBook
    queryset = ReviewBook.objects.all()
    context_object_name = 'reviews_book'
    template_name = 'reviews.html'


class ReviewBookCreateView(CreateView):
    model = ReviewBook
    form_class = ReviewBookForm
    success_url = '/'
    template_name = 'book_detail.html'


class ReviewBookDeleteView(DeleteView):
    model = ReviewBook
    success_url = '/'

