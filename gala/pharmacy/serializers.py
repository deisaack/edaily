from django.contrib.auth.models import User
from rest_framework import serializers

from gala.pharmacy.models import Staff, Pharmacy, Drug, Disease


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=35)
    password = serializers.CharField()
    login_as = serializers.ChoiceField(choices=["doctor", "pharmacist", "nutritionist", "user"])




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields= "__all__"
        exclude = ("password",)


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Staff
        fields= "__all__"


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields= "__all__"


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields= "__all__"

class DrugSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer()
    class Meta:
        model = Drug
        fields= "__all__"

