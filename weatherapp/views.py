from tkinter.messagebox import NO
import requests
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'India'
    app_id = '23b17beac5cb2df914485b5cacb3e228' #api for the weather forecast.
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params  = {
        'q':city,
        'appid':app_id,
        'units':'metric'
    }
    r = requests.get(url = url,params = params)
    res = r.json()
    print(res)
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day=datetime.date.today()
    context = {
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city
        }
    return render(request,'weatherapp/index.html',context)