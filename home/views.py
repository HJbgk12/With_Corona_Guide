from django.shortcuts import render
from home.geocode import gc


def intro(request):
    lat, lon = gc()
    return render(request, 'home/intro.html', {'lat': lat, 'lon' : lon})


def stepbystepRecovery(request):
    return render(request, 'home/stepbystepRecovery.html')


def overseasTripInfo(request):
    return render(request, 'home/overseasTripInfo.html')

