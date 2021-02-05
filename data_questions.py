#https://opentdb.com/api.php?amount=10&type=multiple

import requests


req = requests.get("https://opentdb.com/api.php",params={"amount": 10, "type": "multiple"})
req.raise_for_status()
data = req.json()
print(data)
all_questions = data


