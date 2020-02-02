import requests 
import json
from datetime import datetime
import config

weather_loc = config.WEATHER_LOC

def data():

    url = f'http://api.openweathermap.org/data/2.5/forecast?id={config.WEATHER_LOC}&units=metric&appid={config.OW_API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data


def temp(data, ran):

    r = data
    main =  r['list'][ran]['main']['temp']
    # weather = data['list'][i]['weather'][0]['description']
    # wind_speed = data['list'][i]['wind']['speed']
    # wind_dir = data['list'][i]['wind']['deg']
    time = r['list'][ran]['dt']
    # Converts time to GMT+10 by adding 10 hours
    time = time + 36000
    time = int(time)

    time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    # print('Weather for ' + time)
    # print(main)
    return main, time


def wind(data, ran):
    r = data
    wind_speed = r['list'][ran]['wind']['speed']
    wind_speed = str(int(wind_speed)*3.6)
    wind_dir = r['list'][ran]['wind']['deg']
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(wind_dir / (360. / len(dirs)))
    wind_dir = dirs[ix % len(dirs)]

    return wind_speed, wind_dir

def weather(data, ran):
    r= data
    weather = r['list'][ran]['weather'][0]['description']
    return weather