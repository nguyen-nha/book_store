from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book_name} - {self.writer}'

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name= 'comments')
    owner_of_comment = models.CharField(max_length=255)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book} - {self.comment}'
