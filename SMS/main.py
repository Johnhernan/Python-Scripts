import requests
import datetime as dt

api_key = "foo"
api_call = "https://api.openweathermap.org/data/2.5/onecall"

if __name__ == '__main__':
    weather_params={
        "lat": 18.187607,
        "lon": -66.463251,
        "appid": api_key,
        "exclude":"current,minutely,daily"
    }
    response = requests.get(api_call, params=weather_params)
    response.raise_for_status()
    data = response.json()

    weather_hours = data["hourly"]
    now = dt.datetime.now()
    hour = now.hour

    will_it_rain = False
    for hour in weather_hours[hour: hour+12]:
        weather_at_hour = hour["weather"]
        weather_id = weather_at_hour[0]["id"]
        if weather_id < 700:
            will_it_rain = True
            break


    if will_it_rain:
        print("Bring an umbrella")

    else:
        print("Weather is clear today")