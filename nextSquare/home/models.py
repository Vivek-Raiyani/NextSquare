from django.db import models

class Persons(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add other fields as needed
