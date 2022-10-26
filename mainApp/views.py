from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import City
from .forms import CityForm

def about(request):
    return render(request, 'main.html')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# def weather(request):
#
#     global city_weather
#     cityes = City.objects
#     url = 'https://www.google.com/search?q={}&oq={}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         form.save()
#     form = CityForm()
#     weather_data = []
#     for city in cityes:
#         city_weather = requests.get(url.format(city))
#     soup = BeautifulSoup(city_weather.text, 'html.parser')
#     location = soup.select('#wob_loc')[0].getText()
#     time = soup.select('#wob_dts')[0].getText()
#     info = soup.select('#wob_dc')[0].getText()
#     weath = soup.select('#wob_tm')[0].getText()
#     weather = {
#         'location': location,
#         'time': time,
#         'info': info,
#         'weather': weath
#     }
#     weather_data.append(weather)
#     context = {'weather_data': weather_data, 'form': form}
#     return render(request, 'weather.html', context)
def weather(request):

    cityes = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5973931b289c84dcfc954aebde5165a5'
    # if request.method == 'POST':
    #     form = CityForm(request.POST)
    #     form.save()
    form = CityForm()
    weather_data = []
    for city in cityes:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }
        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather.html', context)
