from django.urls import path
from api.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]
