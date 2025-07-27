# Create a book instance

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
>>> book.title, book.author, book.publication_year
# <Book: 1984 by George Orwell (1949)># Retrieve the created book

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)# Update the Book title

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title, book.author, book.publication_year
# ('Nineteen Eighty-Four', 'George Orwell', 1949)from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>