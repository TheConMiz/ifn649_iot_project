from django.shortcuts import render
from django.http import JsonResponse
from preprocessing.models import *
from preprocessing.views import *
import requests

# Create your views here.
def getProcessedData(request):

    # Call API call in preprocessing here. 
    getAPIData()    

    # Prepare Context for UI Page.
    peripherals_list = list(Peripheral.objects.values())

    current_humidity = Humidity_Reading.objects.latest('time_stamp')
    current_air_quality = Air_Quality_Reading.objects.latest('time_stamp')
    current_temperature = Temperature_Reading.objects.latest('time_stamp')

    context = {
        "peripherals_list": peripherals_list,
        "current_humidity": current_humidity,
        "current_air_quality": current_air_quality,
        "current_temperature": current_temperature,
    }

    return render(request, "cloud_ui/index.html", context)

def getSettings(request):
    return render(request, "cloud_ui/settings.html")

def getTrendsPage(request):
    return render(request, "cloud_ui/trends.html")

def getTrends(request):

    data = []
    labels = []

    query = Air_Quality_Reading.objects.all()

    for item in query:
        data.append(item.pm25_value)
        labels.append(item.time_stamp.time())

    context = {
        "labels": labels,
        "data": data,
    }
    
    return JsonResponse(data=context)