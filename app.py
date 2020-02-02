import config
import weather as wp
from surf import surf
from sms import message
from twilio.rest import Client

data = wp.data()
text = ''
time = []
temp = []
wind = []
weather =[]
for i in range(0,4):
    t = wp.temp(data, i)[1]
    # print('Time = ' + time)

    tem = wp.temp(data, i)[0]
    # print('Temp = ' + str(temp) + 'c')
    cloud = wp.weather(data, i)
    ws = wp.wind(data, i)[0]
    wd = wp.wind(data,i)[1]
    win = wd + ' ' + str(ws) + 'km/h'
    # print('Wind = ' + wd + ' ' + str(ws) + 'km/h')
    time.append(str(t))
    temp.append(str(tem))
    wind.append(win)
    weather.append(cloud)

print(f'The time is {time[0]} and the temp is {temp[0]} and the wind is {wind[0]}')

s_time = []
s_dir = []
s_min = []
s_max = []
s_period = []

for i in range(2,7):
    surf1 = surf(config.SPOT_ID, '1', '3', i)
    surf_time = surf1[0]
    s_time.append(surf_time)

    surf_direction = surf1[1]
    s_dir.append(surf_direction)

    surf_min = surf1[2]
    s_min.append(surf_min)
    
    surf_max = surf1[3]
    s_max.append(surf_max)

    surf_period = surf1[4]
    s_period.append(surf_period)

#Body of the sms
message = f'''
This Morning's Weather: \n
{time[0]} 
{temp[0]} 
{wind[0]}
{weather[0]}

{s_time[0]}
Surf Min: {s_min[0]}m
Surf Max:{s_max[0]}m
Surf Dir: {s_dir[0]}
Surf Period: {s_period[0]}s
            
'''
# Send sms
account_sid = config.TWILIO_SSID
auth_token = config.TWILIO_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body=message,
        from_= config.FROM,
        to= config.TO
    )

print(message.sid)