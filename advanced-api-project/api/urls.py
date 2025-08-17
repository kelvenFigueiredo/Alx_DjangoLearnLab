from django.urls import path
from api.views import BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, BookListView

# URL patterns for the API endpoints related to books
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view   (), name='book-delete'),
]