import config 
import requests
import json
import pandas as pd
import datetime
from datetime import datetime


def surf(spotid, days, hourinterval, i):
    url = 'https://services.surfline.com/kbyg/spots/forecasts/wave'
    payload = {
        'spotId': spotid,
        'days': days,
        'intervalHours': hourinterval
    }
    r = requests.get(url, params=payload)
    d = r.json()
    swell = []
    
    # Each day has 4 intervals so get the number of days and multiply by 4
    # This will need to be changed if you use anything except for 6 hour intervals
    # i = int(days) * 4

    data = r.json()['data']['wave'][i]
    direction = data['swells'][0]['direction']
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(direction / (360. / len(dirs)))
    direction = dirs[ix % len(dirs)]
    s_min = data['surf']['min']
    s_max = data['surf']['max'] 
    period = data['swells'][0]['period']
    time = data['timestamp'] + 36000
    time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

    return time, direction, s_max, s_min, period




# SpotID can be found on surfline.com
spot = '5842041f4e65fad6a7708be8' 

# Days in which you want the forecast for
days = '1'

# Hour intervals that you want the data for
# I set mine to 6 as I found that the forecast was done in 6 hour intervals
interval = '6'

# print(surf(spot, days, interval))