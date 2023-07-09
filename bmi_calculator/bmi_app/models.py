from django.db import models

# Create your models here.

class BMI(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    mobilenumber = models.PositiveIntegerField()

    def __str__(self):
        return self.name



