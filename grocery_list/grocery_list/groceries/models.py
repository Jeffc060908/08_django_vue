from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class GList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    groceries = models.ManyToManyField(Grocery)
    date_of_creation = models.DateTimeField()
    
    class Meta: ordering = ['name']
