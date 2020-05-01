from django.db import models
from django.utils import timezone


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.GenericIPAddressField(max_length=100, null=True, blank=True)
    doctor = models.CharField(max_length=100, null=False, blank=False)
    products = models.TextField()


class Staff(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    dob = models.DateField(blank=True)
    links=["doctor", "nurse", "chemist", "pharmacist"]
    designation=models.CharField(default="doctor", max_length=20)
    created = models.DateTimeField(default=timezone.now)
    location = models.GenericIPAddressField(max_length=100, null=True, blank=True)
