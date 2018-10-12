from django.shortcuts import render
import requests

def home(request):
	print(12345)
	response = requests.get('http://freegeoip.net/json/')
	geodata = response.json()
	context =  {'ip':geodata['ip'],'country':geodata['country_name']}
	return render(request,'template/home.html',context)