from django.shortcuts import render
# from bs4 import BeautifulSoup
import requests, time, pytz
from .models import City
from .forms import CityForm

def start(request):
    form = CityForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def weather(request):

    # cityes = City.objects.last()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5973931b289c84dcfc954aebde5165a5'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []
    cityes = City.objects.last()

    city_weather = requests.get(url.format(cityes)).json()
    country = city_weather['sys']['country']
    current_time_zone = pytz.timezone('Europe/Moscow')
    temperature = (float(city_weather['main']['temp']) - 32) // 1.8
    sunrise = city_weather['sys']['sunrise']
    time_sunrise = time.strftime('%H:%M', time.gmtime(sunrise))
    sunset = city_weather['sys']['sunset']
    time_sunset = time.strftime('%H:%M', time.gmtime(sunset))
    weather = {
        'city': cityes,
        'temperature': temperature,
        'description': city_weather['weather'][0]['description'],
        'humidity': city_weather['main']['humidity'],
        'pressure': city_weather['main']['pressure'],
        'sunrise': time_sunrise,
        'sunset': time_sunset,
        'windspeed': city_weather['wind']['speed']
    }
    weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather.html', context)

