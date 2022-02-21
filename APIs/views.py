from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
import json

@api_view(['GET'])
def getAllDevicesData(request):

    data = []

    for key in cache.keys("*"):
        value = cache.get(key)
        data.append(json.loads(value))
    
    return Response(data)


@api_view(['GET'])
def getDeviceDataById(request, device_id):

    data = cache.get(device_id)

    if data:
        data = json.loads(data)
        return Response(data)
    
    return Response("Device details not found in Cache!")