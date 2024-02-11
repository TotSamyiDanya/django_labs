from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
