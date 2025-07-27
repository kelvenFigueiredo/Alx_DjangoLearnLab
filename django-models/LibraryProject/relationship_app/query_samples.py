from relationship_app import Author, Book, Library, Librarian

# Query all books by a specific  author
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print("Books by author_name:", books_by_author)

# 2. List all books in a library
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# 3. Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of Central Library:", librarian)