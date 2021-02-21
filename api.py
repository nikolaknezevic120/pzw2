import requests

def dataweather():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'zadar', 'appid': 'bd62128bfda0efc6224032f105075a21', 'lang':'hr', 'units':'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return weather