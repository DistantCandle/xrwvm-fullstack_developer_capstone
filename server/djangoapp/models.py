# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    '''
    - Create a car model Django model `class CarModel(models.Model)`
    - Many-to-one relationship to `CarMake` model (One car make can have many car models, using a ForeignKey field)
    - Dealer ID (IntegerField) refers to a dealer created in Cloudant database
    - Name
    - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, and Wagon)
    - Year (IntegerField)
    - Any other fields you would like to include in a car model
    - A `__str__` method to print the car make and car model object
    '''
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) # Many-to-One relationship 

    name = models.CharField(max_length=100) 

    CAR_TYPES = [ 
        ('SEDAN', 'Sedan'), 
        ('SUV', 'SUV'), 
        ('WAGON', 'Wagon'), 
        # Add more choices as required 
    ] 

    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV') 
    year = models.IntegerField(default=2023, validators=[ MaxValueValidator(2023), MinValueValidator(2015) ]) # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation