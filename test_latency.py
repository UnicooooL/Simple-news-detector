import requests
import time
import csv

URL = "http://serve-sentiment-env.eba-fkss5nn8.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    "Breaking: the president has resigned due to scandal",
    "NASA successfully launches new satellite to study Mars",
    "Celebrity claims drinking bleach cures illness",
    "Economic growth reaches record high this quarter"
]

results = []

for case_id, text in enumerate(test_cases, start=1):
    for i in range(100):
        start = time.time()
        response = requests.post(URL, json={"message": text})
        end = time.time()
        latency_ms = (end - start) * 1000
        results.append([case_id, text, i + 1, latency_ms])

with open("latency_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["CaseID", "Text", "Run#", "Latency(ms)"])
    writer.writerows(results)

print("✅ Saved latency_results.csv")
