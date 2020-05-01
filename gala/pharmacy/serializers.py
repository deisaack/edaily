from rest_framework import serializers

from gala.pharmacy.models import Staff, Pharmacy


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=35, default=None)
    password = serializers.CharField()


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields= "__all__"



class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacy
        fields= "__all__"
