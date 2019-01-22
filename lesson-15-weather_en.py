import requests
import json

city = input('What is your city: ')


req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=8ba5aae0a1dd25f3de5d91a05013388c')
weather = json.loads(req.text)


#print(tempo)


print('weather condition:',weather["weather"][0]["main"])
print('temperature(fahrenheit):{:.2f}'.format((float(weather["main"]["temp"]) - 273.15) * (9/5) + 32))
