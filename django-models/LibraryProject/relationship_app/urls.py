from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout', LogoutView.as_view(template_name='relationship_app/logout.html'), name='relationship_app/logout'),
    path('register', views.register_view, name='register')
]
