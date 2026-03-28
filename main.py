import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

api_key=os.environ.get("API_KEY")
city="Shanghai"
lalon_data=requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=c23f404ecd26a19b6ae040feff3d8913")
lalon_data.raise_for_status()
lat=lalon_data.json()[0]["lat"]
lon=lalon_data.json()[0]["lon"]
lalon=(lat,lon)
print(lalon)

parameters={
    "lat":lat,
    "lon":lon,
    "appid":api_key,
    "cnt":4
}
weather_data=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
weather_data.raise_for_status()
weather_list=[]
rain=False
for n in range(4):
    weather=weather_data.json()["list"][n]["weather"][0]["id"]
    print(weather)
    weather_list.append(weather)
    if weather<700:
        rain=True

if rain:
    print("Remember to bring an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to have rain today, remember to bring an umbrella!☔️",
        from_="+18147780719",
        to="+8613479002771",
    )

    print(message.status)
else:
        print("Do not need an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="No umbrella!☔️",
        from_="+18147780719",
        to="+8613479002771",
    )
    print(message.status)

    
