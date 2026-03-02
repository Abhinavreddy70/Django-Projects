from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    discount = models.IntegerField()
    stock_available=models.IntegerField()
    image = models.ImageField(upload_to='product/',null=True, blank=True)

    def __str__(self):
        return self.name
    

class reviews(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.IntegerField()
    def __str__(self):
        return self.review
