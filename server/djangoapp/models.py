from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# CarModel model
class CarModel(models.Model):
    # Choices for the car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship with CarMake
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=50, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015), 
            MaxValueValidator(2023)
            ]
    )

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
