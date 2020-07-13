from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'created_date', 'author', 'image', 'pages', 'headquarter', 'deleted']
