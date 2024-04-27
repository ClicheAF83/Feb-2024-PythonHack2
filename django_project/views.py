
from django.shortcuts import render
import requests
import random

def about(request):
  # Logic for rendering about.html
  return render(request, 'about.html')

def contact(request):
  # Logic for rendering contact.html
  return render(request, 'contact.html')

def home(request):
  # USING APIS create an app that will display the probability it rains in Nairobi


  api_key = 'fcdcd146f22bc05fff5200a1e24df0cd'
  city = 'Nairobi'
  base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

  response = requests.get(base_url)
  data = response.json()

  result = data.get('rain', {'1h': 'No rain in the next hour'})['1h']

  if result == 'No rain in the next hour':
      print('Wow!! Look like you can go out and enjoy the weather')
  else:
      print('The clouds are gathering. It is raining soon')
  



  # Example 2
  reponse2 = requests.get('https://type.fit/api/quotes')
  data2 = reponse2.json()
  result2 = random.choice(data2)['text']


  
  return render(request, 'templates/index.html', {'result': result, 'result2': result2})
  
