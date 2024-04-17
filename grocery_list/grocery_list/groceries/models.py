from django.db import models

# Create your models here.

class grocery_list(models.Model) :
    date_of_creation = models.DateTimeField()
    
    
class grocery(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits= 5, decimal_places=2, default= 0.00)
    
    def __str__(self):
        return self.name    
    
    