from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')