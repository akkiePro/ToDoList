from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    uid = models.IntegerField()

    def __str__(self):
        return self.text


class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
