import requests
import datetime
import os



GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 183
AGE = 29

APP_ID = (os.environ['app_id'])
API_KEY = (os.environ['app_key'])




headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

body = {
    "query": input("Did you exercise today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}




response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=body, headers=headers)
result = response.json()
exercises = result['exercises']
print(exercises)
print(exercises[0]['name'])


#______________________________________________________SHEETY_________________________________________________________________
#BASIC AUTHENTICATION
authsheety = (os.environ['username'], os.environ['password'])

date = datetime.datetime.now()
today = date.strftime("%d/%m/%Y")
time = date.strftime("%I:%M %p")

for exercise in exercises:

    message = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }



    print(message["workout"])
    sheety = requests.post(url="https://api.sheety.co/efa26c7a2f09c24a4779fd46dc2b0fcf/myWorkouts/workouts", json=message, auth=authsheety)
    sheety_response = sheety.json()
    print(sheety_response)