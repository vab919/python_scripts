'#This project makes GET, POST calls to REST API interface and parses API response'
import requests


response = requests.post('http://api.openweathermap.org/data/2.5/forecast', data={'vk':'d26f426b48224ac89beee093fea06f6f'})

print(response.status_code)

print(response.url)

print(response.text)

#response = requests.get('https://api.github.com/events')

