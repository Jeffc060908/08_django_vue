from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=50, unique=True)
    groceries = models.ManyToManyField(Grocery)
    date_of_creation = models.DateTimeField()
    
    class Meta: ordering = ['name']