import urllib.parse

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view, permission_classes, parser_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser


# @api_view(["post"])
# @permission_classes([permissions.AllowAny])
# @parser_classes([FormParser, JSONParser])
@csrf_exempt
def ussd_callback(request):
    body=request.body.decode("utf-8")
    body=urllib.parse.unquote(body)
    body=body.split("&")
    phoneNumber=None
    serviceCode=None
    text=None
    resp=None
    for key in body:
        if "phoneNumber" in key:
            phoneNumber = key.replace("phoneNumber=", "")
            continue
        if "serviceCode" in key:
            serviceCode=key.replace("serviceCode=", "")
            continue
        if "text" in key:
            text=key.replace("text=", "")
            continue
        if "sessionId" in key:
            sessionId=key.replace("sessionId=", "")
            continue
        if "networkCode" in key:
            networkCode=key.replace("networkCode=", "")
            continue
    if text == "":
        resp = "CON What would you want to check \n1. Diseases \n2. Covid19"
    # elif text == "1":
    #     resp = "Get information on\n1. Diabetes\n2. Hypertesion\n3. Kidney issues\n4.Heart Issues"
    elif text == "1*1":
        resp = "CON Diabetes\n1. Nutrition/Diet\n2.Food near you\3. Pharmacies"
    elif text == "1*2":
        resp = "CON Hypertesion\n1. Nutrition/Diet\n2.Food near you\3. Pharmacies"
    elif text == "1*3":
        resp = "CON Kidney issues\n1. Nutrition/Diet\n2.Food near you\3. Pharmacies"
    elif text == "1*4":
        resp = "CON Heart Issues\n1. Nutrition/Diet\n2.Food near you\3. Pharmacies"
    elif text in ["1*5*1", "1*4*1", "1*3*1", "1*2*1", "1*1*1", "1*2"]:
        resp = "END The information will be sent to you shortly"
    else:
        # resp = f"END Invalid option {text} {body}"
        resp = f"CON Invalid option {text} {body}"
    return HttpResponse(resp)
