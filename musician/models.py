from django.core.validators import MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.PositiveIntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def clean(self):
        if self.age < 14:
            raise ValidationError("We do not accept people who are under 14.")

    @property
    def is_adult(self):
        return self.age >= 21

    def __str__(self):
        return self.first_name + " " + self.last_name
