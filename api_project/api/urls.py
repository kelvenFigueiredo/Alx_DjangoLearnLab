from django.urls import path
from api.views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework.authtoken import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Include the router URLs
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),  # Default token auth view
]
