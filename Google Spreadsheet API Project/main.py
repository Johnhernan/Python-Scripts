import requests
import datetime as dt

APP_ID = "foo"
APP_KEY = "foo"

if __name__ == '__main__':
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    sheety_endpoint = "https://api.sheety.co/59c0f2b911791f146f323ff5d7d1fd5a/workouts/workouts"

    exercise_headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }

    exercise_text = input("Tell me which exercises you did: ")

    post = {
     "query": exercise_text,
     "weight_kg": 72.5,
     "height_cm": 167.64,
     "age": 30
    }

    response = requests.post(exercise_endpoint, json=post, headers=exercise_headers)
    response.raise_for_status()
    data = response.json()

    today = dt.datetime.now()
    date = today.strftime("%Y/%m/%d")

    sheety_headers = {
        "Authorization": "foo"
    }

    for exercise in data["exercises"]:
        sheety_params = {
            "workout": {
                "date": date,
                "time": exercise["duration_min"],
                "exercise": exercise["user_input"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(sheety_endpoint, json=sheety_params, headers=sheety_headers)
        print(response.text)
