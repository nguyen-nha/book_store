from django.urls import path
from books.api.views import BooklistCreateAPIView

urlpatterns = [
    path('books', BooklistCreateAPIView.as_view(), name="book-list")
]
