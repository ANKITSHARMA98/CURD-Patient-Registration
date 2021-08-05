from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=22)
    Last_name = models.CharField(max_length=22)
    Gender = models.CharField(max_length=22)
    Age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(103)])
    Disease = models.CharField(max_length=220)
    Doctor_name = models.CharField(max_length=100)
    Doctor_fees = models.IntegerField(default=500)
    Med_date = models.DateField()
    