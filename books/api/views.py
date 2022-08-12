from rest_framework.generics import GenericAPIView
from books.models import Book
from books.api.serializers import BookSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class BooklistCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):

