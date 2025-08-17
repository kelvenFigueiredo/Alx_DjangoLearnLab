from django.contrib import admin
from api.models import Author, Book


# Register your models here.
# AuthorAdmin is used to manage Author model instances in the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_year')
    search_fields = ('title',)
    list_filter = ('publication_year', 'author')
    ordering = ('-publication_year',)
    raw_id_fields = ('author',)

# BookAdmin is used to manage Book model instances in the admin interface
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
