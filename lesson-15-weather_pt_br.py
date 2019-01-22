import requests
import json


cidade = input('Qual a sua cidade: ')

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade + '&appid=8ba5aae0a1dd25f3de5d91a05013388c')
tempo = json.loads(req.text)


#print(tempo)


print('Condição do tempo:',tempo["weather"][0]["main"])
print('temperatura(celsius):{:.2f}'.format(float(tempo["main"]["temp"]) - 273.15)) #celsius
