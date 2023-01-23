from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Biography(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)  # Только один автор


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)  # Может быть много авторов


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
