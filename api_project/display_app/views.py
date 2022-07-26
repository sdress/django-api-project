from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime, date, timedelta
from django.conf import settings

# Create your views here.
def index(request):
    key = settings.NASA_API_KEY
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    nasa_data = response.json()
    # print(nasa_data)
    return render(request, 'index.html', {
        'title': nasa_data['title'],
        'date': datetime.strptime(nasa_data['date'], '%Y-%m-%d').strftime('%m/%d/%Y'),
        'hdurl': nasa_data['hdurl'],
        'explanation': nasa_data['explanation'],
        'credit': nasa_data['copyright']
    })

def previous(request):
    key = settings.NASA_API_KEY
    previous = date.today() - timedelta(days=1)
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}&date={previous}')
    nasa_data = response.json()
    print(nasa_data)
    return render(request, 'index.html', {
        'title': nasa_data['title'],
        'date': datetime.strptime(nasa_data['date'], '%Y-%m-%d').strftime('%m/%d/%Y'),
        'hdurl': nasa_data['hdurl'],
        'explanation': nasa_data['explanation'],
        # TODO: try/except if 'copyright' exists in nasa_data
        # 'credit': nasa_data['copyright']
    })