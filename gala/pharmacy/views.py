from django.shortcuts import render
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


@api_view(["post"])
@permission_classes([permissions.AllowAny])
def ussd_callback(request):
    print("received this data", request.data)
    return Response("CON What would you want to check \n1. My Account \n2. My Balance \n")
