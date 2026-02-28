from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class franchise(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=10)
    founded_year=models.IntegerField()
    no_of_trophies=models.IntegerField()
    logo=models.ImageField(upload_to='franchise_logos/', blank=True,null=True)
    city=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    coach=models.CharField(max_length=100)


    class Meta:
        db_table='franchises'
        

    def __str__(self):
        return f"{self.name}({self.short_name})"
    
#player models

class Player(models.Model):
    ROLE_CHOICES=[
        ('Batsman','Batsman'),
        ('Bowler','Bowler'),
        ('All-rounder','All-rounder'),
        ('Wicket-keeper','Wicket-keeper'),
    ]
    name=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField()
    role=models.CharField(max_length=100 , choices=ROLE_CHOICES)  
    nationality=models.CharField(max_length=100)
    Franchise=models.ForeignKey(franchise,on_delete=models.CASCADE,related_name='players')  
    photo=models.ImageField(upload_to='player_photos/', blank=True,null=True)

    def __str__(self):
        return f"{self.name}({self.role})"



class stadium(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    capacity=models.PositiveIntegerField()
    home_team=models.ForeignKey(franchise,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pictures/', blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"