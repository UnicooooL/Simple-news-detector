import requests

URL = "http://serve-sentiment-env.eba-fkss5nn8.us-east-2.elasticbeanstalk.com/predict"

# URL = "http://your-env-name.eba-xxxxxx.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    "Breaking: the president has resigned due to scandal",  # fake
    "NASA successfully launches new satellite to study Mars",  # real
    "Celebrity claims drinking bleach cures illness",  # fake
    "Economic growth reaches record high this quarter"  # real
]

for text in test_cases:
    response = requests.post(URL, json={"message": text})
    print(f"Input: {text}\nStatus Code: {response.status_code}\nPrediction: {response.json()}\n")
