from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey



# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    gender = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    favoritefood = models.CharField(max_length=40)
    favoritetoy = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name    
    
class Breed(models.Model):
    name = models.CharField(max_length=40)
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    size = models.CharField(choices=SIZE_CHOICES, max_length=6)
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name