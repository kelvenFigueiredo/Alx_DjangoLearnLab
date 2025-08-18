from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# BookCreateView allows authenticated users to create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Automatically set the publication year to the current year if not provided
    def perform_create(self, serializer):
        if not serializer.validated_data.get('publication_year'):
            from datetime import datetime
            serializer.validated_data['publication_year'] = datetime.now().year
        serializer.save()

# BookListView lists all books, accessible to authenticated users or read-only for others.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #adding filtering, searching, and ordering capabilities
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter by title, author, and publication year
    filterset_fields = ['title','author', 'publication_year']

    # Search by title and author name
    search_fields = ['title', 'author__name']

    # Allow ordering by publication year and title
    ordering_fields = ['publication_year', 'title']

    # Default ordering by publication year
    ordering = ['publication_year']  # Default ordering by publication year

# BookDetailView retrieves details of a specific book by its primary key
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookUpdateView allows authenticated users to update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Automatically set the title to 'Untitled' if not provided
    def perform_uptate(self, serializer):
        if serializer.validated_data.get('title') is None:
            serializer.validated_data['title'] = 'Untitled'
        serializer.save()

# BookDeleteView allows authenticated users to delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]