from django.db import models

# Create your models here.

class grocery_list(models.Model) :
    date_of_creation = models.DateTimeField()
    
    
class grocery(models.Model):
    name = models.CharField(max_length = 50)
    
    
