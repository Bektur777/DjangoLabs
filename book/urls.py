from django.urls import path
from book.views import *

urlpatterns = [
    path('', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('book/add-review', ReviewBookCreateView.as_view(), name='review_book'),
    path('book/<int:pk>/update-review', ReviewBookUpdateView.as_view(), name='review_book'),
    path('book/<int:pk>/delete-review', ReviewBookDeleteView.as_view(), name='review_book'),
    path('book/reviews', ReviewBookListView.as_view()),
    path('book/search/', Search.as_view(), name='search'),
]
