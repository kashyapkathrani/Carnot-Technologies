from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
import json


@api_view(['GET'])
def getDeviceData(request, device_id):
    # utils.processCSV()
    data = cache.get(device_id)

    if data:
        data = json.loads(data)
        return Response(data)
    
    return Response("Device details not found in Cache!")