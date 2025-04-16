import requests

NUTRITIONIX_APP_ID = "8d18888c"
NUTRITIONIX_API_KEY = "a286daddff35f19c1547cf22769d9ee9	"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

query = input("What exercise did you do today?: ")
params = {
    "query": query
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)

print(response.json())

