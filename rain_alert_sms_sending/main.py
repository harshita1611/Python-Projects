import requests
import os
from twilio.rest import Client

from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
OMW_endpoint=os.environ.get("OMW_ENDPOINT")
api_key=os.environ.get("OWM_API_KEY")
weather_params={
    "lat": 41.258652,
    "lon": -95.937187,
    "appid": api_key,
    "exclude": "current,minutely,daily"
    }

response=requests.get(OMW_endpoint, params=weather_params)
print(response.raise_for_status)
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice :
  condition_code=hour_data["weather"][0]["id"]
  if condition_code < 700:
    will_rain=True

if will_rain:
  print("Bring an umbrella")

if weather_data["hourly"][0]["weather"][0]["id"] < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
              .create(
                body="It's going to rain today. Remember to bring an ☔",
                from_='+16185911930',
                to='+919408120235'
              )
    print(message.status)
                