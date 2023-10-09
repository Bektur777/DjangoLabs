from django.urls import path
from book.views import *

urlpatterns = [
    path('books', BookListView.as_view()),
]
