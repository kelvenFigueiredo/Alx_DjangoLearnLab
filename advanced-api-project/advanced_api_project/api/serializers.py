from .models import Book, Author
from rest_framework import serializers
from datetime import datetime

# BookSerializzer is used to serialize Book model instances
class BookSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author']

    #validate that title is not empty
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value
    #validate that publication_date is not in the future
    def validate_publication_date(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value
        

# AuthorSerializer is used to serialize Author model instances
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    #validate that name is not empty
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value
