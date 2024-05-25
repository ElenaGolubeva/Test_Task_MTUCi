import requests

data = {"name": ["value1", "value2", "value3", "value4", "value5", "value6"]}

response = requests.post("http://localhost:8000/data", json=data)
print(response.json())