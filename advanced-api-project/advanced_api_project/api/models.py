from django.db import models

# Create your models here.
# Author model represents an author with a name
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Book model represents a book with a title, publication date, and a foreign key to the Author model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.title} ({self.publication_date})"
