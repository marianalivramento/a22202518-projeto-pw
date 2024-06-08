from django.shortcuts import render
import requests


# Create your views here.

def lisboa_hoje_view(request):
    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
                'previsao' : response.json(),
                'frases' : response2.json()
            }

    return render(request, 'meteo/index.html', context)

