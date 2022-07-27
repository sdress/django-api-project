from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime, date, timedelta
from django.conf import settings

key = settings.NASA_API_KEY
# Create your views here.
def index(request):
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    nasa_data = response.json()
    print(nasa_data)
    if 'copyright' in nasa_data:
        print(nasa_data['copyright'])
    return render(request, 'index.html', nasa_data)

def previous(request):
    previous = date.today() - timedelta(days=1)
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}&date={previous}')
    nasa_data = response.json()
    print(nasa_data)
    return render(request, 'index.html', nasa_data)