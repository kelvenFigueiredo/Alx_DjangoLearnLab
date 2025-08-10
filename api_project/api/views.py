from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer