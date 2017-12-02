import json
import requests

json_data=json.dumps({"1": {"value": 4324, "weight": 10180, "volume": 12, "items": [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0]}, "2": {"value": 4372, "weight": 9419, "volume": 13, "items": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]}})
print(json_data)
url ='https://cit-home1.herokuapp.com/api/ga_homework'
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json_data,headers=headers)
print(r.json())