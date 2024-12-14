from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=32)
    place=models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField()

class Book(models.Model):
    title=models.CharField(max_length=100)
    publication_year=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.FloatField(default=0)
