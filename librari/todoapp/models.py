from django.db import models
from authapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    repository = models.URLField(null=True)
    users = models.ManyToManyField(User)


class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)
    active = models.BooleanField(default=True)
