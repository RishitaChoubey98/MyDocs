import geocoder
import requests
import json
import pyttsx3 as p

g = geocoder.ip('me')

engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
              str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        p.speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        p.speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        p.speak('weather type ' + weather_desc['main'])
        p.speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        p.speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        p.speak('Humidity is ' + str(main['humidity']))


if __name__ == '__main__':
    weather()
