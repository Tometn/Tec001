import requests

INPUT = str(input(">>> "))

request = "http://127.0.0.1:5000/get_weather/" + INPUT
response = requests.get(request).json()

print(response)
