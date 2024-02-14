from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persons(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    age = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    TYPE_CHOICES = (
        ('renter', 'Renter'),
        ('landlord', 'Landlord'),
    )
    type_of_user = models.CharField(max_length=8, choices=TYPE_CHOICES)
    #id_proof = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    profile_img= models.ImageField(null=True,blank=True)

class Properties(models.Model):
    property_id = models.AutoField(primary_key=True)
    landlord = models.ForeignKey(Persons, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    property_images = models.TextField()
    property_details = models.TextField()
    renting_amount = models.DecimalField(max_digits=10, decimal_places=2)
    services_subscription_active = models.BooleanField()

class Rentals(models.Model):
    rental_id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(Persons, on_delete=models.CASCADE)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    TENURE_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )
    tenure = models.CharField(max_length=7, choices=TENURE_CHOICES)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    total_rent = models.DecimalField(max_digits=10, decimal_places=2)
    last_payment_date = models.DateField()
    last_payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    new_payment_date = models.DateField()

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(Persons, on_delete=models.CASCADE)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    renter = models.ForeignKey(Persons, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    rental = models.ForeignKey(Rentals, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    mode_of_payment = models.CharField(max_length=50)
    SUCCESS_CHOICES = (
        ('success', 'Success'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    success_status = models.CharField(max_length=7, choices=SUCCESS_CHOICES)
    bank = models.CharField(max_length=255)