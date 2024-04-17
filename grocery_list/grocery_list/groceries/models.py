from django.db import models

# Create your models here.


    
    
class grocery(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
class GList(models.Model) :
    name = models.CharField(max_length=50, unique=True)
    groceries = models.ManyToManyField(grocery)
    date_of_creation = models.DateTimeField()

