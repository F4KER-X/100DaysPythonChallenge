import requests
from datetime import datetime

APP_ID = ""
API_KEY = "	"
TOKEN = ""
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("What exercise did you do?: "),
    "gender": "male",
    "weight_kg": "63",
    "height_cm": "176",
    "age": "22"
}
nutritionix_endpoint = ""

response = requests.post(url=nutritionix_endpoint, json=body, headers=headers)
response.raise_for_status()

data = response.json()
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
exercise = data["exercises"][0]['name']
duration = data["exercises"][0]['duration_min']
calories = data["exercises"][0]['nf_calories']

sheet_url = ""

sheet_content = {'workout':
                 {'date': today,
                  'time': time,
                  'exercise': exercise.title(),
                  'duration': duration,
                  'calories': calories,
                  }}

bearer_headers = {"bearer_headers": f"Bearer {TOKEN}"}
sheet_response = requests.post(
    sheet_url, json=sheet_content, headers=bearer_headers)
sheet_response.raise_for_status()
