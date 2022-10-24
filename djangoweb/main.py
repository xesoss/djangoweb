from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

def about(request):
    return render(request, 'main.html')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(request):

    city = request.GET['city']
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')
    time = soup.select('#wob_dts')
    info = soup.select('#wob_dc')
    weath = soup.select('#wob_tm')
    weather_ = weath
    return render(request, 'weather.html', {'location_': location, 'time_': time, 'info_': info, 'weather__': weather_})
# def weather(request):
#
#     api_key = "5973931b289c84dcfc954aebde5165a5"
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     city_name = request.GET['city']
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#     response = requests.get(complete_url)
#     x = response.json()
#     y = x["main"]
#     temperature = y["temp"]
#     pressure = y["pressure"]
#     humidity = y["humidity"]
#     z = x["weather"]
#     description = z[0]["description"]
#     return render(request, 'weather.html', {'temperature': temperature, 'pressure': pressure, 'humidity': humidity,
#                                             'description': description})
