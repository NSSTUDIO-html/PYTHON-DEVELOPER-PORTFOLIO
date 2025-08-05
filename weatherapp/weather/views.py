import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()

        api_key = '99566ad11be10d487a099354ed836146'


        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            error = "City not found. Please try again."

    return render(request, 'weather/index.html', {
        'weather': weather_data,
        'error': error
    })
