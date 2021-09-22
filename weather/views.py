from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3709035ba3c7c8752f31d959f6694b92').read()
        json_data=json.loads(res)
    
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str("{0:.2f}".format(json_data['main']['temp']-273.15))+'C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
       
      
    else:
        city = ''
        data = {}
    return render(request,'index.html',{'city':city,'data':data})