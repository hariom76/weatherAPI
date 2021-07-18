from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import requests

def index(request):
    if request.method =='POST':
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=f04e7921189e74b4ee6048260e1f13ae'
        city = request.POST['city']
        r = requests.get(url.format(city)).json()
        #send_mail(
         #    'Subject here',
          #   'u have successsfully made a view to'+str(city),
           #  settings.EMAIL_HOST_USER,
           # ['hariommandal76@gmail.com'],
            # fail_silently=False
            # )   
        print(r)
        weather = {
            'city':city,
            'cord1':r['coord']['lon'],
            'cord2':r['coord']['lat'],
            'icon':r['weather'][0]['icon'],
            'temp':r['main']['temp'],
            'weat':r['weather'][0]['description']
        }
        context={'weather':weather}
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')    