import requests
# I updated this to make direct calls to the API

url = "https://opentdb.com/api.php?amount=5&category=9&type=boolean"
response = requests.get(url)
j = response.json()

question_data = j['results']