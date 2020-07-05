from django.db import models


# Create your models here.
class Item(models.Model):
    itemId = models.CharField(unique=True, max_length=100)
    itemName = models.CharField(max_length=100)
    itemPrice = models.FloatField()
    itemStock = models.IntegerField()
    pIMG1 = models.ImageField(upload_to='productinfo')
    pIMG2 = models.ImageField(upload_to='productinfo')
    pIMG3 = models.ImageField(upload_to='productinfo')
    
    def __str__(self):
        return self.itemName
    
