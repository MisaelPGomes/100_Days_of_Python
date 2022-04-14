import requests
from twilio.rest import Client

account_sid = "AC35089a3e457b01cd4fc6067619fc69d9"
auth_token = "c036f3ba751984d582b221c8e6b8058e"

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
apy_key = "c0d24bcd58c116b0ecbcabd8b34ebf9b"
parameters = {
    "lat": -3.732714,
    "lon": -38.526997,
    "appid": apy_key,
    "exclude": "current,minutely,daily"
}
connection = requests.get(OWN_ENDPOINT, params=parameters)
connection.raise_for_status()
data = connection.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain. Get yourself an unbrella",
        from_='+19404003417',
        to='+5585981829988'
    )

    print(message.status)



