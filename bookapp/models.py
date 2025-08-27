from django.db import models

# Create your models here.

class bookapp(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    genre = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}{self.author}"