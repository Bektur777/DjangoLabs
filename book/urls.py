from django.urls import path
from book.views import *

urlpatterns = [
    path('', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('add-review', ReviewBookCreateView.as_view(), name='review_book'),
    path('<int:pk>/delete-review', ReviewBookDeleteView.as_view(), name='review_book'),
    path('reviews', ReviewBookListView.as_view())
]
