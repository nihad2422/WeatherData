from django.shortcuts import render, HttpResponse
import json
import urllib.request

# Create your views here.


def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                     city+'&appid=1339254e48e58b9a94e871b900eaf026&units=metric').read()
        json_data = json.loads(res)  # Here we get the json data

        # Now we need to convert this json data into actual values as following
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']),
            'temperature': str(json_data['main']['temp'])+' Degree Celsius',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }

        context = {'data': data, 'city': city}
    else:
        data = {}
        city = ''
        context = {'data': data, 'city': city}

    return render(request, 'home.html', context)
