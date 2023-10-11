from django.urls import path
from book.views import *

urlpatterns = [
    path('', BookListView.as_view()),
]
