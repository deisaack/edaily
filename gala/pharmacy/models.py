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
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Disease(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=4)


class Drug(models.Model):
    name = models.CharField(max_length=30)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class USSDQuery(models.Model):
    name = models.CharField(max_length=30)
    sesion_id = models.CharField(max_length=50, unique=True)
    content = models.TextField(default="")
