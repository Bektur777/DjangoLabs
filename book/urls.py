from django.urls import path
from book.views import *

urlpatterns = [
    path('', BookListView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view(), name='detail_book')
]
