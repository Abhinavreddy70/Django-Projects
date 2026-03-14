from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # discount should allow decimal values; use DecimalField rather than IntegerField
    discount = models.DecimalField(max_digits=5, decimal_places=2,)
    available_quantity = models.IntegerField()
    image= models.ImageField(upload_to='items/', blank=True, null=True)
    

    def __str__(self):
          return self.name