# Update the Book title

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title, book.author, book.publication_year
# ('Nineteen Eighty-Four', 'George Orwell', 1949)