from django.db import models


class Repair(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class User(models.Model):
    # Добавете полета според вашите нужди
    username = models.CharField(max_length=255)
    # Други полета ...

    def __str__(self):
        return self.username