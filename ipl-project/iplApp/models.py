from django.db import models

# Create your models here.
class franchises(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=10)
    founded_year=models.IntegerField()
    no_of_trophies=models.IntegerField()
    logo=models.ImageField(blank=True,null=True)
    city=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    coach=models.CharField(max_length=100)


    class Meta:
        db_table='franchises'


    def __str__(self):
        return f"{self.name}({self.short_name})"