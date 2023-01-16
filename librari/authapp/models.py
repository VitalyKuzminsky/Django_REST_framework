from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.username}: {self.first_name} {self.last_name}'
