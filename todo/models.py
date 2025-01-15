from django.db import models

# Create your models here.


class Todo(models.Model):
    todo_title = models.CharField(max_length=100)
