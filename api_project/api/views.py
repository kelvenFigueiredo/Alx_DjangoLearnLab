from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly



# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser] # Only allow admin users to modify books