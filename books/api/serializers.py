from rest_framework import serializers
from books.models import Book, Comment

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = "__all__"

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = "__all__"
