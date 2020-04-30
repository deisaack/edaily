from django.shortcuts import render
from rest_framework.decorators import action, api_view, permission_classes, parser_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser


@api_view(["post"])
@permission_classes([permissions.AllowAny])
@parser_classes([FormParser, JSONParser])
def ussd_callback(request):
    print("received this data", request.data)
    return Response("CON What would you want to check \n1. My Account \n2. My Balance \n")
