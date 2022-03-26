import requests

URL = "https://opentdb.com/api.php"
PARAMETERS = {
    'amount': 10,
    'type': "boolean"
}

request = requests.get(URL, PARAMETERS)
question_data = request.json()['results']
