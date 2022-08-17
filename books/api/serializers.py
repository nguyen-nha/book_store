from rest_framework import serializers
from books.models import Book, Comment


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BookSerializer(serializers.Serializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
