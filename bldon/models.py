import datetime
from django.db import models
from django.utils import timezone

class BloodGroup(models.Model):
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Donor(models.Model):
    name = models.CharField(max_length= 100 )
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length= 50)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    gender = models.CharField(max_length=10)
    last_donate = models.DateField(default = timezone.now(), blank= True)

    def __str__(self):
        return self.name
