from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.IntegerField(default=0)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name
