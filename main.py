import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""
FROM_NUMBER = ""
TO_NUMBER = ""
WHATSAPP_PHONE_NUMBER = ""

parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "cnt": 4,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()["hourly"]
weather_slice = data[:12]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
    whatsapp_message = client.messages.create(
        from_=f"whatsapp:{WHATSAPP_PHONE_NUMBERR}",
        body="It's going to rain today. Remember to bring an umbrella ️☂️",
        to=f"whatsapp:{TO_NUMBER}"
    )
    print(message.status)
    print(whatsapp_message.status)
